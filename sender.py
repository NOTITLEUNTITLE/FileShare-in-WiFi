from airshare import sender


# 텍스트 전송
# sender.send_server(code='notitle', text='hello')

# 파일 전송
# sender.send_server(code='notitle', file="pinkoctopus.PNG")

# 폴더 전송
sender.send_server(code='notitle', file="./transfer_test_dir/")