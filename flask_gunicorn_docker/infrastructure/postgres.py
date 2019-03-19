from sqlalchemy.orm.session import sessionmaker


class PostgresService(object):
    def __init__(self, master: sessionmaker, slave: sessionmaker):
        self._master = master()
        self._slave = slave()

    def execute_on_master(self, clause: str, params=None, mapper=None, bind=None, **kw):
        try:
            if self._master.is_active is None:
                self._master.begin()
                ret_val = self._master.execute(clause, params, mapper, bind, **kw)
                self._master.commit()
            else:
                ret_val = self._master.execute(clause, params, mapper, bind, **kw)
        except Exception as e:
            self._master.rollback()
            raise e
        finally:
            self._master.close()

        return ret_val

    def execute_on_slave(self, clause: str, params=None, mapper=None, bind=None, **kw):
        return self._slave.execute(clause, params, mapper, bind, **kw)
