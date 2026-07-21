def first_fit(items, capacity=1.0):
    bins = []              # Remaining space in each bin
    bin_contents = []

    for item in items:
        placed = False

        for i, space in enumerate(bins):
            if space >= item:
                bins[i] -= item
                bin_contents[i].append(item)
                placed = True
                break

        if not placed:
            bins.append(capacity - item)
            bin_contents.append([item])

    return bin_contents


def first_fit_decreasing(items, capacity=1.0):
    return first_fit(sorted(items, reverse=True), capacity)


def best_fit_decreasing(items, capacity=1.0):
    sorted_items = sorted(items, reverse=True)

    bins = []
    bin_contents = []

    for item in sorted_items:
        best_idx = -1
        best_space = float("inf")

        for i, space in enumerate(bins):
            if space >= item and (space - item) < best_space:
                best_space = space - item
                best_idx = i

        if best_idx != -1:
            bins[best_idx] -= item
            bin_contents[best_idx].append(item)
        else:
            bins.append(capacity - item)
            bin_contents.append([item])

    return bin_contents


def display_bins(title, bins):
    print(f"\n{title}: {len(bins)} bins")

    for i, b in enumerate(bins, start=1):
        used = sum(b)
        bar = "#" * int(used * 20)

        print(
            f"Bin {i}: {[round(x,1) for x in b]} "
            f"| Used: {used:.1f} "
            f"[{bar:<20}]"
        )


# ---------------- Main Program ----------------

items = [0.5, 0.7, 0.3, 0.9, 0.2, 0.6, 0.8, 0.4, 0.1, 0.5]
capacity = 1.0

# Lower bound on number of bins
lower_bound = int(-(-sum(items) // capacity))

print("Items:", items)
print("Bin Capacity:", capacity)
print("Total Size of Items:", sum(items))
print("Lower Bound on Bins:", lower_bound)

ff_bins = first_fit(items)
ffd_bins = first_fit_decreasing(items)
bfd_bins = best_fit_decreasing(items)

display_bins("First Fit (FF)", ff_bins)
display_bins("First Fit Decreasing (FFD)", ffd_bins)
display_bins("Best Fit Decreasing (BFD)", bfd_bins)

print("\nSummary")
print(f"Lower Bound = {lower_bound}")
print(f"First Fit (FF) = {len(ff_bins)} bins")
print(f"First Fit Decreasing (FFD) = {len(ffd_bins)} bins")
print(f"Best Fit Decreasing (BFD) = {len(bfd_bins)} bins")