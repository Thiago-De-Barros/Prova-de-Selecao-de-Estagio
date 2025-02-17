from BD import engine
import modelos

modelos.Base.metadata.create_all(bind=engine)