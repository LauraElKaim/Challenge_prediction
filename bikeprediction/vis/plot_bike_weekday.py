import matplotlib.pyplot as plt
import seaborn as sns

def plot_weekday(self):
    df = self[(self["Hour"] < "09:30:00") & (self["Hour"] > "08:30:00")]
    df = df.drop_duplicates(subset = ['Date'], keep = 'last')
    mond_df = df[df['Weekday'] == 0]
    tues_df = df[df['Weekday'] == 1]
    wedn_df = df[df['Weekday'] == 2]
    thur_df = df[df['Weekday'] == 3]
    frid_df = df[df['Weekday'] == 4]
    satu_df = df[df['Weekday'] == 5]
    sund_df = df[df['Weekday'] == 6]
    sns.set_palette("bright", n_colors=7)
    plt.figure(figsize=(5000,5000))
    plt.figure()
    plt.plot(mond_df['Date'], mond_df['Number of bikes from 00:01 to the given time'])
    plt.plot(tues_df['Date'], tues_df['Number of bikes from 00:01 to the given time'])
    plt.plot(wedn_df['Date'], wedn_df['Number of bikes from 00:01 to the given time'])
    plt.plot(thur_df['Date'], thur_df['Number of bikes from 00:01 to the given time'])
    plt.plot(frid_df['Date'], frid_df['Number of bikes from 00:01 to the given time'])
    plt.plot(satu_df['Date'], satu_df['Number of bikes from 00:01 to the given time'])
    plt.plot(sund_df['Date'], sund_df['Number of bikes from 00:01 to the given time'])
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    plt.xlabel("Date")
    plt.ylabel("Number of bicyle passages")
    plt.title("Number of bicycle passages from midnight to between 8:30 and 9:30 according to the date")
    plt.legend(labels=days, loc='lower left', bbox_to_anchor=(1, 0.2))
    plt.show()
    return df