import sqlite3

from entity.Agent import Agent


class AgentRepository:
    conn = sqlite3.connect('bitprop.db')
    cur = conn.cursor()

    @classmethod
    def create(cls, agent: Agent):
        with cls.conn:
            cls.cur.execute("INSERT INTO agent VALUES (null, :first_name, :last_name, :email_address, :username, "
                            ":password)",
                            {'first_name': agent.first_name, 'last_name': agent.last_name,
                             'email_address': agent.email_address, 'username': agent.username,
                             'password': agent.password})

    @classmethod
    def read(cls, agent_id):
        cls.cur.execute("SELECT * FROM agent WHERE agent_id = :agent_id", {'agent_id': agent_id})
        return cls.cur.fetchone()

    @classmethod
    def delete(cls, agent_id):
        with cls.conn:
            cls.cur.execute("DELETE FROM agent WHERE agent_id = :agent_id", {'agent_id': agent_id})

    @classmethod
    def read_all(cls):
        cls.cur.execute("SELECT * FROM agent")
        return cls.cur.fetchall()
