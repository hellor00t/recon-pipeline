from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, String, Table

from .base_model import Base


port_association_table = Table(
    "port_association",
    Base.metadata,
    Column("port_id", Integer, ForeignKey("port.id")),
    Column("target_id", Integer, ForeignKey("target.id")),
)


class Port(Base):
    """ Database model that describes a port (tcp or udp).

        Relationships:
            ``targets``: many to many -> :class:`models.target_model.Target`
    """

    __tablename__ = "port"

    id = Column(Integer, primary_key=True)
    protocol = Column(String)
    port_number = Column(Integer)
    target_id = Column(Integer, ForeignKey("target.id"))
    targets = relationship("Target", secondary=port_association_table, back_populates="open_ports")
