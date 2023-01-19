import uvicorn
from fastapi import FastAPI
from fastapi_crudrouter import SQLAlchemyCRUDRouter

from model import customer, autoparts, mechanic
from schema import customer_schema, autoparts_schema, mechanic_schema
from util.db_conexion import Base, engine, get_db

Base.metadata.create_all(bind=engine)

# Creating a router for the Customer model.
Customer_router = SQLAlchemyCRUDRouter(
    schema=customer_schema.Customer,
    create_schema=customer_schema.CustomerCreate,
    db_model=customer.CustomerModel,
    db=get_db,
    prefix="Customer",
    get_all_route=True,
    delete_all_route=False,
)


# Creating a router for the Mechanic model.
Mechanic_router = SQLAlchemyCRUDRouter(
    schema=mechanic_schema.Mechanic,
    create_schema=mechanic_schema.MechanicCreate,
    db_model=mechanic.MechanicModel,
    db=get_db,
    prefix="Mechanic",
    get_all_route=True,
    delete_all_route=False,
)

# Creating a router for the AutoPart model.
Autoparts_router = SQLAlchemyCRUDRouter(
    schema=autoparts_schema.AutoPart,
    create_schema=autoparts_schema.AutoPartCreate,
    db_model=autoparts.AutoPartModel,
    db=get_db,
    prefix="autorpart",
    get_all_route=True,
    delete_all_route=False,
)


app = FastAPI()

# Adding the routes to the app.
app.include_router(Customer_router)
app.include_router(Mechanic_router)
app.include_router(Autoparts_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
