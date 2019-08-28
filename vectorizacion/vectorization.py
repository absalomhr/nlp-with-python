def load_dict(filename):
    import numpy as np
    dict = np.load(filename, allow_pickle=True).item()
    return dict

def save_dict(filename):
    import numpy as np
    # Save dict to disk
    np.save(filename+'.npy', dict)

