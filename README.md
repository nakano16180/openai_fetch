## openai gym practice


```
$ sudo apt install libosmesa6-dev libgl1-mesa-glx libglfw3

```

after clone this repository
```
$ pipenv install
$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/nakano/.mujoco/mujoco210/bin
$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/nvidia
$ export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so

$ pipenv run sample.py
```


- https://github.com/openai/mujoco-py/issues/652
- https://github.com/openai/mujoco-py/issues/268
    - export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so