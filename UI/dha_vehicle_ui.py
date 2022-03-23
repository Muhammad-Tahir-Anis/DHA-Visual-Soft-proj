from tkinter import *
from tkinter import ttk, filedialog
from tkinter.ttk import Combobox

from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import DateEntry

from BL.get_and_insert_data import folder_to_database_data_insertion
from BL.graph import bar_graph_one_day_by_hours, bar_graph_one_week_by_hours, bar_graph_one_week_by_days


def select_folder(file):
    folder = filedialog.askdirectory()
    file.set(folder)


class HomePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="First Page")
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Graphs", command=lambda: controller.show_frame(GraphPage))
        button.pack(side=TOP)

        # File Selection
        file_selection_label = Label(self)
        file_selection_label.pack(side=TOP, anchor=N)
        # Cont...
        file = StringVar()
        select_folder_label = Entry(file_selection_label, textvariable=file)
        select_folder_label.pack(side=LEFT, anchor=N)
        # Cont...
        select_folder_button = ttk.Button(file_selection_label, text="Select Folder",
                                          command=lambda: select_folder(file))
        select_folder_button.pack(side=LEFT, anchor=N)

        # Insert Data Section
        insert_data_button = ttk.Button(self, text="Insert Data", command=lambda: self.insert_data(file))
        insert_data_button.pack(side=TOP, anchor=N)

        self.progress_bar = ttk.Progressbar(self, orient="horizontal", mode="determinate")
        self.progress_bar.pack(side=TOP, anchor=N, expand=True, fill="x", padx=10)

    def insert_data(self, file):
        folder_to_database_data_insertion(file.get(), self.progress_bar)
        self.progress_bar.stop()


class GraphPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.figure = None
        # Title of Page on Top
        title_label = Label(self, text="Graph Page!")
        title_label.pack(pady=10, padx=10)

        # Home Page
        button = ttk.Button(self, text="Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

        # Options Section
        options_label = Label(self)
        options_label.pack(side=TOP, anchor=N)
        # Graph Selection
        graph_selection_row_label = Label(options_label)
        graph_selection_row_label.pack(side=LEFT, anchor=N)
        # Cont...
        graph_label = Label(graph_selection_row_label, text="Select Graph")
        graph_label.pack(side=TOP, anchor=W)
        # Cont...
        select_graph = StringVar(graph_selection_row_label, "Select Graph")
        my_graphs = ["bar graph 1 day by hours",
                     "bar graph 1 week by days",
                     "bar graph 1 week by hours"]
        graph_selector = Combobox(graph_selection_row_label, textvariable=select_graph, values=my_graphs,
                                  state="readonly", width=25)
        graph_selector.pack(side=TOP, anchor=W)

        # Date Selection
        date_selection_row_label = Label(options_label)
        date_selection_row_label.pack(side=LEFT, anchor=N)
        # Cont...
        date_label = Label(date_selection_row_label, text="Select Date")
        date_label.pack(side=TOP, anchor=W)
        # Cont..
        calendar = DateEntry(date_selection_row_label, dateformat=3, width=10, background='white',
                             foreground='black', borderwidth=4)
        calendar.pack(side=TOP, anchor=W)

        # DHA Phase Selection
        phase_selection_row_label = Label(options_label)
        phase_selection_row_label.pack(side=LEFT, anchor=N)
        # Cont...
        phase_label = Label(phase_selection_row_label, text="Select Phase")
        phase_label.pack(side=TOP, anchor=W)
        # Cont...
        select_phase = StringVar(phase_selection_row_label, "Select Graph")
        my_phases = ["None", "1", "2", "3", "4"]
        phase_selector = Combobox(phase_selection_row_label, textvariable=select_phase, values=my_phases,
                                  state="readonly", width=25)
        phase_selector.pack(side=TOP, anchor=W)

        # Button To Show Graph
        button = ttk.Button(self, text="Show Graph", command=lambda: self.change_graph(fig_canvas, calendar.get_date(),
                                                                                       graph_selector.get(),
                                                                                       phase_selector.get()))
        button.pack(side=TOP, anchor=N)

        # Graph Canvas
        fig_canvas = Canvas(self, height=500)
        fig_canvas.pack(side=BOTTOM, fill=BOTH, anchor=S)

    def change_graph(self, fig_canvas: Canvas, date: str, graph_type: str, phase_number: str):
        for fig in fig_canvas.winfo_children():
            fig.destroy()
        if graph_type == "bar graph 1 day by hours":
            if phase_number is "" or phase_number == "None":
                self.figure = bar_graph_one_day_by_hours(date)
            else:
                self.figure = bar_graph_one_day_by_hours(date, phase_number)
        elif graph_type == "bar graph 1 week by days":
            if phase_number == "" or phase_number == "None":
                self.figure = bar_graph_one_week_by_days(date)
            else:
                self.figure = bar_graph_one_week_by_days(date, phase_number)
        elif graph_type == "bar graph 1 week by hours":
            if phase_number is "" or phase_number == "None":
                self.figure = bar_graph_one_week_by_hours(date)
            else:
                self.figure = bar_graph_one_week_by_hours(date, phase_number)
        graph_canvas = FigureCanvasTkAgg(self.figure, fig_canvas)
        # graph_canvas.get_tk_widget().pack(side=TOP, fill=BOTH)
        toolbar = NavigationToolbar2Tk(graph_canvas, fig_canvas)
        toolbar.update()
        graph_canvas.get_tk_widget().config(height=500)
        graph_canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH)


class DHAVehicleDataAnalysisApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        Tk.wm_title(self, "DHA Vehicle Data Analysis App")

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        pages = [HomePage, GraphPage]

        for page in pages:
            frame = page(container, self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


app = DHAVehicleDataAnalysisApp()
app.mainloop()
