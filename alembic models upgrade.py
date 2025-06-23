# # 初始化的脚本
# alembic init alembic



# # 第1次执行的脚本
# alembic revision --autogenerate -m "Initial tables"
# alembic upgrade head



# # 后面更新models后执行的脚本
# alembic revision --autogenerate -m "add age column"
# alembic upgrade head