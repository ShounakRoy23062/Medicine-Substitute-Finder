from flask import Flask, render_template, request, redirect, url_for, flash
import os
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.secret_key = "medifind-demo-key"


# ==========================================================
# 1. CONNECT TO MYSQL
# ==========================================================

def connect_database():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="shounak@123",
        database="MediFindDB"
    )


# ==========================================================
# 2. HOME PAGE AND MEDICINE SEARCH
# ==========================================================

@app.route("/", methods=["GET"])
def home():

    medicines = []
    original = None
    substitutes = []
    suppliers = []

    search_name = request.args.get("medicine", "").strip()

    db = None
    cursor = None

    try:
        db = connect_database()
        cursor = db.cursor(dictionary=True)

        # Retrieve all medicines.
        cursor.execute("""
            SELECT Med_ID, Med_Name, Composition, Med_Type, Price
            FROM Det
            ORDER BY Med_ID
        """)

        medicines = cursor.fetchall()

        # Search for a medicine.
        if search_name:

            cursor.execute("""
                SELECT Med_ID, Med_Name, Composition, Med_Type, Price
                FROM Det
                WHERE LOWER(Med_Name) = LOWER(%s)
                LIMIT 1
            """, (search_name,))

            original = cursor.fetchone()

            # Try a partial name match if necessary.
            if original is None:

                cursor.execute("""
                    SELECT Med_ID, Med_Name, Composition, Med_Type, Price
                    FROM Det
                    WHERE LOWER(Med_Name) LIKE LOWER(%s)
                    ORDER BY Med_ID
                    LIMIT 1
                """, (f"%{search_name}%",))

                original = cursor.fetchone()

            if original:

                # Find cheaper medicines with the same composition.
                cursor.execute("""
                    SELECT
                        Med_ID,
                        Med_Name,
                        Composition,
                        Med_Type,
                        Price,
                        ROUND(%s - Price, 2) AS Savings
                    FROM Det
                    WHERE LOWER(Composition) = LOWER(%s)
                      AND Med_ID <> %s
                      AND Price < %s
                    ORDER BY Price ASC
                """, (
                    original["Price"],
                    original["Composition"],
                    original["Med_ID"],
                    original["Price"]
                ))

                substitutes = cursor.fetchall()

                # Find potential suppliers by medicine category.
                categories = ["General"]

                medicine_type = original["Med_Type"].lower()
                composition = original["Composition"].lower()

                if medicine_type == "tablet":
                    categories.append("Tablets")

                elif medicine_type == "capsule":
                    categories.append("Capsules")

                elif medicine_type == "syrup":
                    categories.append("Syrups")

                elif medicine_type == "injection":
                    categories.append("Injections")

                if composition == "azithromycin":
                    categories.append("Antibiotics")

                placeholders = ", ".join(["%s"] * len(categories))

                cursor.execute(f"""
                    SELECT
                        Supplier_ID,
                        Supplier_Name,
                        City,
                        Contact_No,
                        Supply_Type
                    FROM Supplier
                    WHERE Supply_Type IN ({placeholders})
                    ORDER BY Supplier_ID
                """, tuple(categories))

                suppliers = cursor.fetchall()

            else:
                flash(
                    "Medicine not found. Please enter a valid medicine name.",
                    "error"
                )

    except Error as err:
        app.logger.exception("Database operation failed")
        return (
            f"<h2>Database connection or query failed</h2>"
            f"<p>{str(err)}</p>",
            500
        )

    finally:
        if cursor is not None:
            cursor.close()

        if db is not None and db.is_connected():
            db.close()

    # Display the HTML page.
    return render_template(
        "user.html",
        medicines=medicines,
        original=original,
        substitutes=substitutes,
        suppliers=suppliers,
        search_name=search_name
    )


# ==========================================================
# 3. ADD A NEW MEDICINE
# ==========================================================

@app.route("/insert", methods=["POST"])
def insert_medicine():

    med_name = request.form.get("med_name", "").strip()
    composition = request.form.get("composition", "").strip()
    med_type = request.form.get("med_type", "").strip()
    price_text = request.form.get("price", "").strip()

    # Validate the form.
    if not all([med_name, composition, med_type, price_text]):
        flash("Please fill in all medicine fields.", "error")
        return redirect(url_for("home"))

    try:
        price = float(price_text)

        if price < 0:
            flash("Price cannot be negative.", "error")
            return redirect(url_for("home"))

    except ValueError:
        flash("Please enter a valid price.", "error")
        return redirect(url_for("home"))

    db = None
    cursor = None

    try:
        db = connect_database()
        cursor = db.cursor()

        # Generate the next ID and insert the record.
        cursor.execute("""
            INSERT INTO Det
                (Med_ID, Med_Name, Composition, Med_Type, Price)
            SELECT
                COALESCE(MAX(Med_ID), 0) + 1,
                %s, %s, %s, %s
            FROM Det
        """, (
            med_name,
            composition,
            med_type,
            price
        ))

        db.commit()

        flash("Medicine added successfully!", "success")

    except Error as err:

        if db is not None and db.is_connected():
            db.rollback()

        app.logger.exception("Medicine insertion failed")
        flash(f"Could not add medicine: {err}", "error")

    finally:
        if cursor is not None:
            cursor.close()

        if db is not None and db.is_connected():
            db.close()

    return redirect(url_for("home"))


# ==========================================================
# 4. START FLASK
# ==========================================================

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)