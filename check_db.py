
import sqlite3

conn = sqlite3.connect("food.db")
cur = conn.cursor()

print("--- First 3 additives ---")
for row in cur.execute("SELECT * FROM additives LIMIT 3"):
    print(row)

print()
print("--- All nutrient thresholds ---")
for row in cur.execute("SELECT * FROM nutrient_thresholds"):
    print(row)

print()
print("--- Count of Harmful vs Caution additives ---")
for row in cur.execute("SELECT category, COUNT(*) FROM additives GROUP BY category"):
    print(row)

conn.close()