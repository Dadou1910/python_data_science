import time
import os
import shutil

def ft_tqdm(lst: range) -> None:
    """ Replicates the behaviour of the tqdm function:
prints a loading bar to the temrinal to notify the 
user of how advanced the program's execution is.
    
Takes a range as argument"""
    total = len(lst)
    start = time.time()

    for i, item in enumerate(lst, 1):
        percent = i / total

        elapsed = time.time() - start
        speed = i / elapsed if elapsed > 0 else 0

        remaining = (total - i) / speed if speed > 0 else 0

        em, es = divmod(int(elapsed), 60)
        rm, rs = divmod(int(remaining), 60)

        time_part = f"{em:02}:{es:02}<{rm:02}:{rs:02}"

        cols = shutil.get_terminal_size(fallback=(80, 20)).columns

        left = f"{int(percent*100):3d}%|["
        right = f"]| {i}/{total} [{time_part}, {speed:6.2f} it/s]"

        bar_len = max(1, cols - len(left) - len(right))

        filled = int(bar_len * percent)

        if filled >= bar_len:
            bar = "=" * bar_len
        else:
            bar = "=" * filled + ">" + " " * (bar_len - filled - 1)
        
        line = (f"\r\033[K{left}{bar}{right}").encode()
        if len(line) >= cols:
            line = line[:cols-1 + 5]
        os.write(1, line)

        yield item

def main():
    for elem in ft_tqdm(range(333)):
        pass

if __name__ == '__main__':
    main()