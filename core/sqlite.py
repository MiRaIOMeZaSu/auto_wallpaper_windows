#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3


conn = sqlite3.connect('d://线上sql/test.db')


def create_db_table():
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "bizhi" (
            "id"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            "name"  TEXT(30),
            "small"  TEXT(100),
            "big"  TEXT(100),
            "local"  TEXT(100),
            "createtime"  TEXT(20)
            );
            
        ''')
    cursor.execute('''CREATE INDEX IF NOT EXISTS "index_bizhi_name" ON "bizhi" ("name" COLLATE RTRIM ASC);''')
    cursor.close()


def delete_db_table():
    cursor = conn.cursor()
    cursor.execute('''SELECT name FROM sqlite_master;''')
    results = cursor.fetchall()
    for row in results:
        try:
            cursor.execute("DROP TABLE "+row[0]+"")
        except Exception as e:
            ...
    cursor.execute("DELETE FROM sqlite_sequence")
    cursor.close()


if __name__ == "__main__":
    create_db_table()
    delete_db_table()