import os
import sys

def trigger_kernel_panic():
    try:
        # Проверяем, имеет ли пользователь root-права
        if os.geteuid() != 0:
            print("Этот скрипт должен быть запущен с правами root.")
            sys.exit(1)
        
        # Запись в /proc/sysrq-trigger для вызова kernel panic
        with open("/proc/sysrq-trigger", "w") as f:
            f.write("c")
    except Exception as e:
        print(f"Не удалось вызвать kernel panic: {e}")

if __name__ == "__main__":
    trigger_kernel_panic()
  #load this with root rights, it will either not start
