def test_db_connection(db):
    assert db.fetch_one("SELECT 1") == (1,)


def test_create_table(db):
    db.create_products_table()
    assert db.count_products() == 0


def test_insert(db):
    db.insert_product("Noir jacket", 55)
    db.insert_product("Grey jacket", 60)
    db.insert_product("Striped top", 50)
    assert db.count_products() == 3


def test_select(db):
    products = db.get_all_products()
    names = [name for name, price in products]
    assert names == ["Noir jacket", "Grey jacket", "Striped top"]


def test_update(db):
    db.update_product_price("Noir jacket", 70)
    assert float(db.get_product("Noir jacket")[1]) == 70


def test_delete(db):
    db.delete_product("Striped top")
    assert db.count_products() == 2