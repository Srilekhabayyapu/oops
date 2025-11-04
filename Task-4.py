import csv
import os
from datetime import datetime
from collections import defaultdict

DATA_DIR = "finance_data"

class Expense:
    def __init__(self, date: datetime, category: str, amount: float, description: str=""):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def to_csv_row(self):
        return [ self.date.strftime("%Y-%m-%d"),
                 self.category,
                 f"{self.amount:.2f}",
                 self.description ]

    @staticmethod
    def from_csv_row(row):
        date = datetime.strptime(row[0], "%Y-%m-%d")
        category = row[1]
        amount = float(row[2])
        description = row[3] if len(row) > 3 else ""
        return Expense(date, category, amount, description)


class FinanceTracker:
    def __init__(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        self.expenses = []  # list of Expense

    def add_expense(self, date: datetime, category: str, amount: float, description: str=""):
        exp = Expense(date, category, amount, description)
        self.expenses.append(exp)
        print(f"Added: {exp.date.date()} | {exp.category} | {exp.amount:.2f} | {exp.description}")

    def load_month(self, year: int, month: int):
        """Load expenses from file for given year/month."""
        fname = self._filename_for_month(year, month)
        path = os.path.join(DATA_DIR, fname)
        self.expenses = []
        if os.path.exists(path):
            with open(path, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    try:
                        e = Expense.from_csv_row(row)
                        self.expenses.append(e)
                    except Exception as ex:
                        print("Error parsing row:", row, ex)
            print(f"Loaded {len(self.expenses)} expenses from {path}")
        else:
            print(f"No data file found for {year}-{month:02d} (expecting {path})")

    def save_month(self, year: int, month: int):
        """Save current expenses list to a file for the given year/month."""
        fname = self._filename_for_month(year, month)
        path = os.path.join(DATA_DIR, fname)
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for e in self.expenses:
                writer.writerow(e.to_csv_row())
        print(f"Saved {len(self.expenses)} expenses to {path}")

    def report_month(self, year: int, month: int):
        """Generate a simple report: total spend, by category, list items."""
        self.load_month(year, month)
        total = sum(e.amount for e in self.expenses)
        by_cat = defaultdict(float)
        for e in self.expenses:
            by_cat[e.category] += e.amount
        print(f"\n*** Report for {year}-{month:02d} ***")
        print(f"Total expenses: {total:.2f}")
        print("By category:")
        for cat, amt in by_cat.items():
            print(f"  {cat}: {amt:.2f}")
        print("\nDetails:")
        for e in sorted(self.expenses, key=lambda x: x.date):
            print(f"{e.date.strftime('%Y-%m-%d')} | {e.category:<15} | {e.amount:8.2f} | {e.description}")
        print("*** End of report ***\n")

    def _filename_for_month(self, year: int, month: int):
        return f"expenses_{year}_{month:02d}.csv"


def main():
    tracker = FinanceTracker()

    while True:
        print("\nOptions:")
        print("  1. Add expense")
        print("  2. Generate monthly report")
        print("  3. Save current month data")
        print("  4. Load a different month")
        print("  5. Exit")
        choice = input("Choose (1-5): ").strip()
        if choice == "1":
            date_str = input("Enter date (YYYY-MM-DD) [default today]: ").strip()
            if not date_str:
                date = datetime.today()
            else:
                try:
                    date = datetime.strptime(date_str, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date format.")
                    continue
            category = input("Category: ").strip()
            if not category:
                print("Category cannot be empty.")
                continue
            try:
                amount = float(input("Amount: ").strip())
            except ValueError:
                print("Invalid amount.")
                continue
            description = input("Description (optional): ").strip()
            tracker.add_expense(date, category, amount, description)

        elif choice == "2":
            ym = input("Enter year-month (YYYY-MM) [default current]: ").strip()
            if not ym:
                year = datetime.today().year
                month = datetime.today().month
            else:
                try:
                    year, month = map(int, ym.split("-"))
                    if not (1 <= month <= 12):
                        raise ValueError
                except:
                    print("Invalid year-month format.")
                    continue
            tracker.report_month(year, month)

        elif choice == "3":
            # Save current expenses to current month
            now = datetime.today()
            tracker.save_month(now.year, now.month)

        elif choice == "4":
            ym = input("Enter year-month to load (YYYY-MM): ").strip()
            try:
                year, month = map(int, ym.split("-"))
                if not (1 <= month <= 12):
                    raise ValueError
            except:
                print("Invalid year-month format.")
                continue
            tracker.load_month(year, month)

        elif choice == "5":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice, please pick 1-5.")

if __name__ == "__main__":
    main()
