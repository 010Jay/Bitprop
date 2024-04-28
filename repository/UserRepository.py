import sqlite3

from entity.User import User


class UserRepository:

    conn = sqlite3.connect('bitprop.db')
    cur = conn.cursor()

    @classmethod
    def create(cls, user: User):
        with cls.conn:
            cls.cur.execute(" INSERT INTO user VALUES (null, :first_name, :last_name, :email_address, :cellphone)",
                            {'first_name': user.first_name, 'last_name': user.last_name,
                             'email_address': user.email_address,
                             'cellphone': user.cellphone})

    @classmethod
    def read(cls, user_id):
        cls.cur.execute("SELECT * FROM user WHERE user_id = :user_id", {'user_id': user_id})
        return cls.cur.fetchone()

    @classmethod
    def delete(cls, user_id):
        with cls.conn:
            cls.cur.execute("DELETE FROM user WHERE user_id = :user_id", {'user_id': user_id})

    @classmethod
    def read_all(cls):
        cls.cur.execute("SELECT * FROM user")
        return cls.cur.fetchall()
