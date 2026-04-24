# bill_estimation_system
using excel and python

# 🧾 Bill Estimation System (Python + Excel)

## 📌 Overview

The **Bill Estimation System** is a Python-based project that calculates the total bill amount based on products, quantity, and price.
It reads data from Excel, performs calculations, and generates a final bill with item-wise details.

This project simulates a real-world billing system used in shops, supermarkets, and online stores.

---

## 🎯 Objectives

* To automate bill calculation using Python
* To handle product data using Excel
* To generate accurate item-wise billing
* To improve efficiency over manual billing

---

## 🚀 Features

* 📥 Read product data from Excel
* 🧮 Calculate total bill automatically
* 🧾 Generate item-wise bill summary
* 💰 Calculate subtotal and total amount
* 💾 Export final bill to Excel

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – data handling
* **OpenPyXL** – Excel operations
* **Microsoft Excel** – data storage

---

## 📁 Project Structure

```id="b2q8mz"
bill-estimation/
│
├── data/
│   └── products.xlsx
│
├── output/
│   └── final_bill.xlsx
│
├── src/
│   └── main.py
│
├── requirements.txt
├── README.md
```

---

## 📊 Dataset Description

The Excel file contains:

| Product | Price | Quantity |
| ------- | ----- | -------- |
| Rice    | 50    | 2        |
| Milk    | 30    | 3        |
| Bread   | 40    | 1        |

* **Product** → Item name
* **Price** → Price per unit
* **Quantity** → Units purchased

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```id="p9x7ut"
git clone https://github.com/your-username/bill-estimation.git
cd bill-estimation
```

### 2️⃣ Install Dependencies

```id="h4k2lv"
pip install -r requirements.txt
```

### 3️⃣ Run the Project

```id="n6w8zr"
python src/main.py
```

---

## 📈 Output

* 🧾 Item-wise bill
* 💰 Total bill amount
* 📄 Excel file with final bill

---

## 📌 Example Output

* Rice → ₹100
* Milk → ₹90
* Bread → ₹40
* **Total → ₹230**

---

## 🔮 Future Enhancements

* Add GST calculation
* Add discount system
* GUI billing system
* Print invoice feature

---

## 👨‍💻 Author

**Agrim Dangi**
Student | Developer

---

## ⭐ Conclusion

This project demonstrates how Python and Excel can be used together to automate billing systems efficiently.

---

## 📎 License

This project is for educational purposes only.
