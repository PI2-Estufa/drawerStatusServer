from nameko.rpc import rpc
import db
from db import DrawerStatus


class DrawerStatusServer():
    name = "drawer_status_server"

    @rpc
    def receive_drawer_status(self, drawer_status):
        drawer_status = round(drawer_status, 1)
        d = DrawerStatus()
        d.value = drawer_status
        try:
            db.session.add(d)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
        return drawer_status