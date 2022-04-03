import time
import os

WINDOW_W = 1000
WINDOW_H = 800

class mySimpleEnv():
    renderer = None
    
    def __init__(self) -> None:
        self.render_obs = [0, 0]
        self.map_path = os.path.dirname(os.path.abspath(__file__)) + '/maps/berlin'
        self.map_ext = '.png'
    
    def update_obs(self, lap_count=0):
        self.render_obs[0] = time.time()
        self.render_obs[1] = lap_count

    
    def step(self):
        pass
    
    
    def reset(self):
        pass
    
    
    def render(self, mode='human'):
        assert mode in ['human', 'human_fast']

        # first call, initialize everything
        if mySimpleEnv.renderer is None:
            from rendering import EnvRenderer
            mySimpleEnv.renderer = EnvRenderer(WINDOW_W, WINDOW_H)
            mySimpleEnv.renderer.update_map(self.map_path, self.map_ext)

        mySimpleEnv.renderer.update_obs(self.render_obs)
        
        mySimpleEnv.renderer.dispatch_events()
        mySimpleEnv.renderer.on_draw()
        mySimpleEnv.renderer.flip()
        
        if mode == 'human':
            time.sleep(0.05)
        elif mode == 'human_fast':
            pass