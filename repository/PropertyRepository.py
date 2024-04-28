import sqlite3

from entity.Property import Property


class PropertyRepository:
    conn = sqlite3.connect('bitprop.db')
    conn.execute("PRAGMA foreign_keys = 1")
    cur = conn.cursor()

    @classmethod
    def create(cls, prop: Property):
        with cls.conn:
            cls.cur.execute("INSERT INTO property VALUES (null, :image, :address, :rental_flats, :available, "
                            ":agent_id)",
                            {'image': prop.image, 'address': prop.address,
                             'rental_flats': prop.rental_flats, 'available': prop.available,
                             'agent_id': prop.agent_id})

    @classmethod
    def read(cls, prop_id):
        cls.cur.execute("SELECT * FROM property WHERE property_id = :prop_id", {'prop_id': prop_id})
        return cls.cur.fetchone()

    @classmethod
    def delete(cls, prop_id):
        with cls.conn:
            cls.cur.execute("DELETE FROM property WHERE property_id = :prop_id", {'prop_id': prop_id})

    @classmethod
    def read_all(cls):
        cls.cur.execute("SELECT * FROM property")
        return cls.cur.fetchall()

    