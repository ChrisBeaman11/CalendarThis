from flask import Blueprint, render_template
import sqlite3
import os
import datetime
bp = Blueprint('main', __name__, '/')
DB_FILE = os.environ.get("DB_FILE")
@bp.route('/')
def main():
    with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor()
        curs.execute('SELECT id, name, start_datetime, end_datetime FROM appointments ORDER BY start_datetime')
        rows = curs.fetchall()
        for row in rows:
            pass
            # print(row)
            datetime_str = row[2]
            datetime_obj = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
            print(f"the datetime_obj {datetime_obj}")
            row +=tuple("".join(tuple(datetime_obj.strftime("%H:%M"))))
            print(row)
        # print(f"these are the rows {rows}")
        return render_template('main.html', rows=rows)
