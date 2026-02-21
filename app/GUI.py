import tkinter as tk
import numpy as np

def brownian_sim_results(mean:float, num_of_sim:int, vol_day:float, ret_day:float):
    root=tk.Tk()
    root.title("reults of the simulation")
    message = f"""
    Monte Carlo Simulation Summary

    Number of simulation runs: {num_of_sim:,}

    Estimated daily return: {ret_day:.6f}
    Estimated annual return: {ret_day * 252 * 100:.2f}%

    Estimated daily volatility: {vol_day:.6f}
    Estimated annual volatility: {vol_day * np.sqrt(252) * 100:.2f}%

    Mean simulated return: {mean:.6f}
    """
    label = tk.Label(root, text=message)
    label.pack()
    
    root.mainloop()