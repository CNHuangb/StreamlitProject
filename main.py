import streamlit as st
from app.database import init_db, get_db
from app.crud.user import create_user, get_users
from sqlalchemy.orm import Session

st.set_page_config(page_title="用户管理系统", layout="wide")



# # 初始化数据库，使用Alembic就不用初始化数据库
# if st.sidebar.button("初始化数据库"):
#     init_db()
#     st.sidebar.success("数据库表已创建")




# 检查数据库是否为最新版本
def check_migrations():
    from alembic.config import Config
    from alembic import command
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

# 在应用启动时检查
check_migrations()









# 主界面
st.title("用户管理系统")

# 添加用户表单
with st.form("user_form"):
    st.subheader("添加新用户")
    name = st.text_input("姓名")
    email = st.text_input("邮箱")
    age = st.number_input("年龄", min_value=0, max_value=120)
    
    submitted = st.form_submit_button("提交")
    
    if submitted:
        db = next(get_db())
        try:
            create_user(db, name=name, email=email, age=age)
            st.success("用户添加成功!")
        except Exception as e:
            st.error(f"添加失败: {str(e)}")

# 显示用户列表
if st.button("显示用户列表"):
    db = next(get_db())
    users = get_users(db)
    if not users:
        st.warning("没有用户数据")
    else:
        st.subheader("用户列表")
        for user in users:
            st.write(f"- {user.name}, {user.email}, {user.age}岁")






























# # app.py
# import streamlit as st
 
# def main():
#     """主函数，定义你的Streamlit应用逻辑"""
#     st.title('Hello, World!')  # 设置标题
#     st.write('这是一个使用Streamlit的简单示例。')  # 显示文字
 
# if __name__ == "__main__":
#     main()


#     if __name__ == '__main__':
#     uvicorn.run("main:app", port=8000, reload=True)




# import streamlit as st
# from streamlit.web.cli import main as st_main
# import sys

# def my_app():
#     st.title("My App")
#     st.write("Hello!")

# if __name__ == "__main__":
#     if len(sys.argv) == 1:
#         sys.argv = ["streamlit", "run", sys.argv[0]]
#     st_main()








# import os
# import signal
# import subprocess
 
# def kill_streamlit_server():
#     # 查找并杀死所有 Streamlit 进程
#     os.system('pkill -f streamlit')
 
# if __name__ == '__main__':
#     kill_streamlit_server()  # 杀死所有 Streamlit 进程
#     subprocess.run(["streamlit", "run", "StreamlitProject/app.py"])  # 重新启动 Streamlit 应用