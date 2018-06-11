from nameko.rpc import rpc
import db
from db import DrawerStatus


class DrawerStatusServer():
    name = "drawer_status_server"

    @rpc
    def receive_drawer_status(self, drawer_status):
        d = DrawerStatus()
        d.value = drawer_status
        db.session.add(d)
        db.session.commit()
        return drawer_status