class PostgresService(object):
    def __init__(self, master, slave):
        self._master = master
        self._slave = slave

    def execute_on_master(self, clause, params=None, mapper=None, bind=None, **kw):
        return self._master.execute(clause, params, mapper, bind, **kw)

    def execute_on_slave(self, clause, params=None, mapper=None, bind=None, **kw):
        return self._slave.execute(clause, params, mapper, bind, **kw)
