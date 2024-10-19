# %%
from rich.console import Console
from time import sleep
import general.loadings as ld
import general.preparation as prep
import general.settings as st
import numpy as np
import analysis.plotter as pl
import analysis.waveform as wf
import matplotlib.pyplot as plt

# def main():
#     """Main function"""
console = Console()
console.print("Starting the analysis", style="bold blue")

with console.status("[bold magenta]Loading the configuration file...[/bold magenta]") as status:
    sleep(1)

    load = ld.Loadings()
    main_directory, date, slice, stim_ch, scale = load.read_config()
    path:str = f"{main_directory}/{date}/slice{slice}"

    console.log(f"[magenta]Configuration file was successfully loaded. [/magenta]")
    sleep(1)

prep.make_folder(path)

with console.status("[bold blue]Loading the csv file ...[/bold blue]") as status:
    sleep(1)

    lfps = load.read_csv(f"{path}/{date}_slice{slice}_ch{stim_ch}.csv")

    console.log(f"[blue]CSV file was successfully loaded. [/blue]")

FS, CHS, DURATION, STIM_TIMING, TRIALS = st.Settings().set_basic_params()
N:int = int(FS * DURATION)

t:np.ndarray[float] = np.arange(0, DURATION, 1/FS) * 1e3  # in ms
averaged_lfps = wf.Waveform().averaged_wave(lfps, CHS, TRIALS, N)

with console.status("[bold green]Plotting LFPs ...[/bold green]") as status:
    sleep(1)

    fig = pl.Figure().plot_lfps(t, averaged_lfps, STIM_TIMING, scale, CHS, stim_ch)

    fig.savefig(f"{path}/Figure/{date}_slice{slice}_ch{stim_ch}_{scale/2}uV.png", bbox_inches="tight")
    plt.clf()
    plt.close()

    console.log(f"[green]LFPs were successfully plotted. [/green]")

# if __name__ == "__main__":
#     main()

# %%
