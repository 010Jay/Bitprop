import sqlite3

from entity.Order import Order


class OrderRepository:
    conn = sqlite3.connect('bitprop.db')
    conn.execute("PRAGMA foreign_keys = 1")
    cur = conn.cursor()

    @classmethod
    def create(cls, order: Order):
        with cls.conn:
            cls.cur.execute(" INSERT INTO orders VALUES (null, :user_id, :property_id)",
                            {'user_id': order.user_id, 'property_id': order.property_id})

    @classmethod
    def read(cls, order_id):
        cls.cur.execute("SELECT * FROM orders WHERE order_id = :order_id", {'order_id': order_id})
        return cls.cur.fetchone()

    @classmethod
    def delete(cls, order_id):
        with cls.conn:
            cls.cur.execute("DELETE FROM orders WHERE order_id = :order_id", {'order_id': order_id})

    @classmethod
    def read_all(cls):
        cls.cur.execute("SELECT * FROM orders")
        return cls.cur.fetchall()

