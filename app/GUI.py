from tkinter import * 
import tkinter as tk
import numpy as np
import stochasticprocess as sp
import csvdatabase as csvd
import normalmodel as nm
class GUI:
    def __init__(self,ver):
        self.version = ver
        self.sday:float = 0
        self.eday:float = 0
        self.ticker:str = ''
        self.numOfSim = 0
        self.daysInFuture = 0
        self.daysInPastToProbe = 0
        
    def main_menu(self):
        root = tk.Tk()
        root.title(f"Stan's Stock Analyzer Version {self.version}")
        message = "Main Menu"
        root.geometry("1000x500")
        label = tk.Label(root, text = message)
        label.grid(row=0, column=5)
        #ticker input
        tk.Label(root, text="Ticker").grid(row=0, column=0)
        self.ticker =tk.Entry(root)
        self.ticker.grid(row=0, column=1)
        # end frame day
        tk.Label(root, text="End Date").grid(row=1, column=0)
        self.eday =tk.Entry(root)
        self.eday.grid(row=1, column=1)
        #start frame day
        tk.Label(root, text="Start Date").grid(row=2, column=0)
        self.sday =tk.Entry(root)
        self.sday.grid(row=2, column=1)
        #number of simulations
        tk.Label(root, text="Number of Simulations").grid(row=3, column=0)
        self.numOfSim =tk.Entry(root)
        self.numOfSim.grid(row=3, column=1)
        #number of days in the future to simulate
        tk.Label(root, text="Number of Days in the Future to simulate").grid(row=4, column=0)
        self.daysInFuture =tk.Entry(root)
        self.daysInFuture.grid(row=4, column=1)
        #number of days in the future to probe
        tk.Label(root, text="Number of Days in the Past to probe").grid(row=5, column=0)
        self.daysInPastToProbe =tk.Entry(root)
        self.daysInPastToProbe.grid(row=5, column=1)
        
        button = tk.Button(root, text="Start Simulation", width=25,command=self.simulate_b_motion)
        button.grid(row=6, column=5)
        
        root.mainloop()
        
    def simulate_b_motion(self):
        try:
            sday = int(self.sday.get())
            eday = int(self.eday.get())
            numOfSim = int(self.numOfSim.get())
            daysInFuture = int(self.daysInFuture.get())
            daysInPastToProbe = int(self.daysInPastToProbe.get())
        except ValueError:
            print("Days must be integers")
            return

        if eday > sday:
            print("invalid days entered")
            return
        ticker_value = self.ticker.get().strip().upper()

        if ticker_value == "":
            print("Ticker cannot be empty")
            return
        
        if daysInFuture == 0:
            print("invalid days in the future entered")
            return
        
        days = sday- eday
        
        d =sp.predict_for_data(ticker_value,days,days,0,0,numOfSim, eday, sday, daysInFuture,daysInPastToProbe)
        mean = nm.bar_model_data(d[0])
        vol_and_ret = d[1]
        self.brownian_sim_results(mean,numOfSim,vol_and_ret[1],vol_and_ret[0])

    def brownian_sim_results(self,mean:float, num_of_sim:int, vol_day:float, ret_day:float):
        top = Toplevel()
        top.title("reults of the simulation")
        message = f"""
        Monte Carlo Simulation Summary

        Number of simulation runs: {num_of_sim:,}

        Estimated daily return: {ret_day:.6f}
        Estimated annual return: {ret_day * 252 * 100:.2f}%

        Estimated daily volatility: {vol_day:.6f}
        Estimated annual volatility: {vol_day * np.sqrt(252) * 100:.2f}%

        Mean simulated return: {mean:.6f}
        """
        label = tk.Label(top, text=message)
        label.pack()
        
        top.mainloop()