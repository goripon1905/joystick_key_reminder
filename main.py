import pygame
import time

pygame.init()

# 接続されてるコントローラーの数を取得
joystick_count = pygame.joystick.get_count()

# コントローラーを指定
target_joystick_index = None
for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    if joystick.get_name() == "Generic USB Joystick":
        target_joystick_index = i
        break

if target_joystick_index is not None:
    # コントローラー初期化
    joystick = pygame.joystick.Joystick(target_joystick_index)
    joystick.init()

    pygame.display.init()

    # キーリマインダー音
    sound = pygame.mixer.Sound("key.wav")
    is_playing = False

    try:
        while True:
            pygame.event.get()
            button_1_state = joystick.get_button(0)  # 1番目のボタン
            button_2_state = joystick.get_button(1)  # 2番目のボタン
            button_3_state = joystick.get_button(2)  # 3番目のボタン
            button_4_state = joystick.get_button(3)  # 4番目のボタン

            # 2,3,4番目のボタンが同時に押されている場合
            if button_2_state == 1 and button_3_state == 1 and button_4_state == 1:
                if is_playing:
                    sound.stop()
                    is_playing = False
            # 1,3,4番目のボタンが同時に押されている場合
            elif button_1_state == 1 and button_3_state == 1 and button_4_state == 1:
                if is_playing:
                    sound.stop()
                    is_playing = False
            elif button_4_state == 1 and not is_playing:
                sound.play(-1)  # ループ再生
                is_playing = True
            elif button_4_state == 0 and is_playing:
                sound.stop()
                is_playing = False

            time.sleep(0.1)  # CPU使用率が跳ね上がるから少し待ってあげる処理

    except KeyboardInterrupt:
        pass
    finally:
        joystick.quit()
        pygame.quit()
else:
    print("エラー:指定のコントローラーが見つかりませんでした。")
