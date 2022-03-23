from datetime import timedelta, datetime

import matplotlib.pyplot as plt
import numpy as np

from DB.db_functions import \
    data_of_week_by_days_entry, \
    data_of_week_by_days_exit, \
    data_of_day_by_hours_entry, \
    data_of_day_by_hours_exit, \
    data_of_week_by_hours_entry, \
    data_of_week_by_hours_exit


def bar_graph_one_day_by_hours(date_from, phase_number=None):
    x_label = "Hours"
    y_label = "Number of Vehicles"
    title = f"DHA Entry and Exit count of Vehicle in 24 Hours by {date_from}"

    entry_data = data_of_day_by_hours_entry(date_from, phase_number)
    exit_data = data_of_day_by_hours_exit(date_from, phase_number)
    x = np.arange(len(entry_data))
    width = 0.45

    # plt.rcParams["figure.figsize"] = 20, 20
    fig, ax = plt.subplots()
    exit_bar = ax.bar(x - width / 2, exit_data, width, label="Exit")
    entry_bar = ax.bar(x + width / 2, entry_data, width, label="Entry")

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_xticks(x, range(1, len(entry_data) + 1))
    ax.set_title(title, fontsize=6)
    ax.set_ylim([0, 3600])
    ax.legend()

    ax.bar_label(exit_bar, padding=3)
    ax.bar_label(entry_bar, padding=3)
    fig.tight_layout()
    plt.tight_layout()
    # plt.show()
    fig.savefig('day graph by hours.png')
    return fig


def bar_graph_one_week_by_days(date_from, phase_number=None):
    start_date = datetime.strptime(str(date_from), "%Y-%m-%d").date()
    x_label = "Days"
    y_label = "Number of Vehicles"
    title = f"DHA Entry and Exit count of Vehicle from {date_from} to {start_date + timedelta(7)}"

    entry_data = data_of_week_by_days_entry(date_from, phase_number)
    exit_data = data_of_week_by_days_exit(date_from, phase_number)
    x = np.arange(len(entry_data))
    width = 0.45
    fig, ax = plt.subplots()
    exit_bar = ax.bar(x - width / 2, exit_data, width, label="Exit")
    entry_bar = ax.bar(x + width / 2, entry_data, width, label="Entry")

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_xticks(x, range(1, len(entry_data) + 1))
    ax.set_title(title, fontsize=6)
    ax.set_ylim([0, 36000])
    ax.legend()

    ax.bar_label(exit_bar, padding=3)
    ax.bar_label(entry_bar, padding=3)
    fig.tight_layout()
    # plt.show()
    fig.savefig('week graph by days.png')
    return fig


def bar_graph_one_week_by_hours(date_from, phase_number=None):
    start_date = datetime.strptime(str(date_from), "%Y-%m-%d").date()
    x_label = "Hours"
    y_label = "Number of Vehicles"
    title = f"DHA Entry and Exit count of Vehicle from {date_from} to {start_date + timedelta(7)}"

    entry_data, date_time_stamps = data_of_week_by_hours_entry(date_from, phase_number)
    exit_data = data_of_week_by_hours_exit(date_from, phase_number)
    x = np.arange(len(entry_data))
    width = 0.45
    plt.rcParams["figure.autolayout"] = True
    plt.rcParams["figure.figsize"] = 15, 5
    # plt.figure(figsize=(20, 3))

    plt.plot()
    fig, ax = plt.subplots()

    # ax.plot(exit_data, 'o--y', linewidth=2)

    exit_bar = ax.bar(x - width / 2, exit_data, width, label="Exit Bar")
    exit_plt = ax.plot(x - width / 2, exit_data, 2, label="Exit Plot")
    entry_bar = ax.bar(x + width / 2, entry_data, width, label="Entry Bar")
    entry_plt = ax.plot(x - width / 2, entry_data, 2, label="Entry Plot")

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_xticks(x, date_time_stamps, rotation=90)
    ax.set_title(title, fontsize=6)
    ax.set_ylim([0, 3000])
    ax.legend()

    ax.bar_label(exit_bar, padding=3, rotation=90)
    ax.bar_label(entry_bar, padding=3, rotation=90)
    fig.tight_layout()
    # plt.show()
    fig.savefig('week graph by hours.png',
                dpi=300,
                facecolor='w',
                edgecolor='w',
                orientation='landscape',
                format=None,
                transparent=False,
                bbox_inches='tight',
                pad_inches=0.1,
                metadata=None)
    return fig