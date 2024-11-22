class Seaborn:
    def __init__(self):
        self.color_palettes = {}
        self.figures = []

    def set_style(self, style):
        print(f"Setting style to {style}...")

    def set_palette(self, palette_name, colors):
        self.color_palettes[palette_name] = colors

    def get_palette(self, palette_name):
        return self.color_palettes.get(palette_name, [])

    def figure(self, width, height):
        return {"width": width, "height": height, "axes": []}

    def axes(self, figure, x_label, y_label):
        axes = {"x_label": x_label, "y_label": y_label, "title": "", "plots": []}
        figure["axes"].append(axes)
        return axes

    def set_title(self, axes, title):
        axes["title"] = title

    def plot(self, axes, plot_type, x_data, y_data=None, labels=None, colors=None):
        axes["plots"].append({
            "type": plot_type,
            "x_data": x_data,
            "y_data": y_data,
            "labels": labels,
            "colors": colors,
        })

    def show(self, figure):
        for axes in figure["axes"]:
            self._plot_graph(figure, axes)

    def _plot_graph(self, figure, axes):
        title_centered = axes["title"].center(figure["width"])
        print(f"\n{title_centered}\n")

        for plot in axes["plots"]:
            plot_type = plot["type"]
            x_data, y_data = plot["x_data"], plot["y_data"]
            labels, colors = plot.get("labels"), plot.get("colors")

            if plot_type == "bar":
                self._plot_bar(figure, x_data, y_data, labels, colors)
            elif plot_type == "scatter":
                self._plot_scatter(figure, x_data, y_data, colors)
            elif plot_type == "line":
                self._plot_line(figure, x_data, y_data, colors)
            elif plot_type == "count":
                self._plot_countplot(figure, x_data, labels, colors)
            elif plot_type == "heatmap":
                self._plot_heatmap(figure, x_data, y_data, colors)
            elif plot_type == "box":
                self._plot_boxplot(figure, x_data, y_data, colors)
            else:
                print(f"Unsupported plot type: {plot_type}")

    def _plot_bar(self, figure, x_data, y_data, labels, colors):
        max_value = max(y_data)
        scale = figure["height"] / max_value

        for i in range(figure["height"], 0, -1):
            row = f"{int(i / scale):<3}| "
            for j, value in enumerate(y_data):
                if value * scale >= i:
                    row += f"{colors[j % len(colors)]}█\033[0m"
                else:
                    row += " "
                row += "   "
            print(row)

        print(" " * 4 + "-" * (len(y_data) * 4))
        print(" " * 4 + " ".join(f"{label:<3}" for label in x_data))

    def _plot_scatter(self, figure, x_data, y_data, colors):
        max_x, max_y = max(x_data), max(y_data)
        scale_x, scale_y = figure["width"] / max_x, figure["height"] / max_y

        for i in range(figure["height"], 0, -1):
            row = f"{int(i / scale_y):<3}| "
            for j in range(figure["width"]):
                found = False
                for k, (x, y) in enumerate(zip(x_data, y_data)):
                    if int(y * scale_y) == i and int(x * scale_x) == j:
                        row += f"{colors[k % len(colors)]}•\033[0m"
                        found = True
                        break
                if not found:
                    row += " "
            print(row)

        print(" " * 4 + "-" * figure["width"])

    def _plot_line(self, figure, x_data, y_data, colors):
        max_x, max_y = max(x_data), max(y_data)
        scale_x, scale_y = figure["width"] / max_x, figure["height"] / max_y

        for i in range(figure["height"], 0, -1):
            row = f"{int(i / scale_y):<3}| "
            for j in range(figure["width"]):
                for k in range(len(x_data) - 1):
                    x1, y1, x2, y2 = x_data[k], y_data[k], x_data[k + 1], y_data[k + 1]
                    if (int(y1 * scale_y) == i and int(x1 * scale_x) == j) or \
                       (int(y2 * scale_y) == i and int(x2 * scale_x) == j):
                        row += f"{colors[k % len(colors)]}-\033[0m"
                        break
                else:
                    row += " "
            print(row)

        print(" " * 4 + "-" * figure["width"])

    def _plot_countplot(self, figure, x_data, labels, colors):
        count_dict = {label: x_data.count(label) for label in set(x_data)}
        labels = list(count_dict.keys())
        y_data = list(count_dict.values())
        self._plot_bar(figure, labels, y_data, labels, colors)

    def _plot_heatmap(self, figure, x_data, y_data, colors):
        for row in y_data:
            print("".join([f"{colors[val % len(colors)]}█\033[0m" for val in row]))

    def _plot_boxplot(self, figure, x_data, y_data, colors):
        median = sorted(y_data)[len(y_data) // 2]
        print(f"Boxplot: Median = {median}")


# Example with User Input
seaborn = Seaborn()
seaborn.set_style("whitegrid")
seaborn.set_palette("deep", ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m"])

figure = seaborn.figure(50, 15)
axes = seaborn.axes(figure, "X-axis", "Y-axis")
seaborn.set_title(axes, "Dynamic Graph")

# User input for plot type
plot_type = input("Enter plot type (bar, scatter, line, count, heatmap, box): ").strip().lower()

if plot_type == "bar":
    x_data = ["A", "B", "C", "D", "E"]
    y_data = [5, 10, 7, 12, 9]
    colors = seaborn.get_palette("deep")
    seaborn.plot(axes, plot_type, x_data, y_data, x_data, colors)
elif plot_type == "scatter":
    x_data = [1, 2, 3, 4, 5]
    y_data = [5, 10, 7, 12, 9]
    colors = seaborn.get_palette("deep")
    seaborn.plot(axes, plot_type, x_data, y_data, colors=colors)
elif plot_type == "line":
    x_data = [1, 2, 3, 4, 5]
    y_data = [5, 10, 7, 12, 9]
    colors = seaborn.get_palette("deep")
    seaborn.plot(axes, plot_type, x_data, y_data, colors=colors)
elif plot_type == "count":
    x_data = ["A", "A", "B", "C", "A", "B", "C", "C", "C", "D"]
    colors = seaborn.get_palette("deep")
    seaborn.plot(axes, plot_type, x_data, labels=None, colors=colors)
elif plot_type == "heatmap":
    x_data = [1, 2, 3]
    y_data = [
        [1, 2, 0],
        [3, 1, 2],
        [2, 4, 3]
    ]
    colors = seaborn.get_palette("deep")
    seaborn.plot(axes, plot_type, x_data, y_data, colors=colors)
elif plot_type == "box":
    x_data = [1, 2, 3, 4, 5]
    y_data = [5, 10, 7, 12, 9]
    colors = seaborn.get_palette("deep")
    seaborn.plot(axes, plot_type, x_data, y_data, colors=colors)
else:
    print(f"Unsupported plot type: {plot_type}")

# Display the figure
seaborn.show(figure)
