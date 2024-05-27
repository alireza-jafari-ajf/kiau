import sqlite3 as sql

conn = sql.connect(database="data.db" , check_same_thread=False)
c = conn.cursor()



def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS article_form_one(first_name TEXT , last_name TEXT , age INTEGER , gender TEXT , education TEXT , job TEXT , use_ai_for_academic_work TEXT ,  tool TEXT , app_or_web TEXT , web_browser TEXT , operating_system TEXT , why_use TEXT , another_reason TEXT , ai_ssp TEXT)")

def add_data(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , web_browser , operating_system , why_use , another_reason , ai_ssp):
    c.execute(f"INSERT INTO article_form_one(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , web_browser , operating_system , why_use , another_reason , ai_ssp) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)" , (first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , web_browser , operating_system , why_use , another_reason , ai_ssp))
    conn.commit()

def add_data1(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work):
    c.execute(f"INSERT INTO article_form_one(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work) VALUES (?,?,?,?,?,?,?)" , (first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work))
    conn.commit()

def add_data2(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , web_browser , ai_ssp):
    c.execute(f"INSERT INTO article_form_one(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , web_browser , ai_ssp) VALUES (?,?,?,?,?,?,?,?,?,?,?)" , (first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , web_browser , ai_ssp))
    conn.commit()

def add_data2_app(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , operating_system , ai_ssp):
    c.execute(f"INSERT INTO article_form_one(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , operating_system , ai_ssp) VALUES (?,?,?,?,?,?,?,?,?,?,?)" , (first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , operating_system , ai_ssp))
    conn.commit()

def add_data2_both(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , web_browser ,  operating_system , ai_ssp):
    c.execute(f"INSERT INTO article_form_one(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , web_browser ,  operating_system , ai_ssp) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)" , (first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , web_browser ,  operating_system , ai_ssp))
    conn.commit()

def add_data3(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , web_browser, why_use , ai_ssp):
    c.execute(f"INSERT INTO article_form_one(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , web_browser , why_use , ai_ssp) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)" , (first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , web_browser , why_use , ai_ssp))
    conn.commit()

def add_data3_app(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , operating_system, why_use , ai_ssp):
    c.execute(f"INSERT INTO article_form_one(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , operating_system , why_use , ai_ssp) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)" , (first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , operating_system , why_use , ai_ssp))
    conn.commit()

def add_data3_both(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , web_browser ,  operating_system, why_use , ai_ssp):
    c.execute(f"INSERT INTO article_form_one(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , web_browser ,  operating_system , why_use , ai_ssp) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)" , (first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , web_browser ,  operating_system , why_use , ai_ssp))
    conn.commit()

def add_data4(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , web_browser , why_use , another_reason , ai_ssp):
    c.execute(f"INSERT INTO article_form_one(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , web_browser , why_use , another_reason , ai_ssp) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)" , (first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , web_browser , why_use , another_reason , ai_ssp))
    conn.commit()

def add_data4_app(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , operating_system , why_use , another_reason , ai_ssp):
    c.execute(f"INSERT INTO article_form_one(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , operating_system , why_use , another_reason , ai_ssp) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)" , (first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , operating_system , why_use , another_reason , ai_ssp))
    conn.commit()


#def add_data2(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , web_browser , operating_system , why_use , another_reason , ai_ssp):
#    c.execute(f"INSERT INTO article_form_one(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , web_browser , operating_system , why_use , another_reason , ai_ssp) VALUES ({first_name} , {last_name} , {age} , {gender} , {education} , {job} ,  {use_ai_for_academic_work} , {tool} , {app_or_web} , {web_browser} , {operating_system} , {why_use} , {another_reason} , {ai_ssp}) ")
#    conn.commit()

def view_all_data():
    c.execute("SELECT * FROM article_form_one")
    data = c.fetchall()
    return data

def view_unique_task():
    c.execute("SELECT DISTINCT last_name FROM article_form_one")
    data = c.fetchall()
    return data

def get_task(task):
    c.execute(f"SELECT * FROM article_form_one WHERE last_name='{task}'")
    data = c.fetchone()
    return data

def edit_task_data(nfirst_name , nlast_name , nage , ngender , neducation , njob ,  nuse_ai_for_academic_work , ntool , napp_or_web , nweb_browser , noperating_system , nwhy_use , nanother_reason , nai_ssp, first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , web_browser , operating_system , why_use , another_reason , ai_ssp):
    c.execute("UPDATE article_form_one SET first_name=? , last_name=? , age=? , gender=? , education=? , job=? , use_ai_for_academic_work=? ,  tool=? , app_or_web=? , web_browser=? , operating_system=? , why_use=? , another_reason=? , ai_ssp=? WHERE first_name=? and last_name=? and age=? and gender=? and education=? and job=? and use_ai_for_academic_work=? and  tool=? and app_or_web=? and web_browser=? and operating_system=? and why_use=? and another_reason=? and ai_ssp=?" , (nfirst_name , nlast_name , nage , ngender , neducation , njob ,  nuse_ai_for_academic_work , ntool , napp_or_web , nweb_browser , noperating_system , nwhy_use , nanother_reason , nai_ssp, first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , web_browser , operating_system , why_use , another_reason , ai_ssp))
    data = c.fetchall()
    return data