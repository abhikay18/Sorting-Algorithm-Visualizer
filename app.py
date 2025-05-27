import streamlit as st
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sorting_algorithms import bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort


def main():
    st.set_page_config(
        page_title="Sorting Algorithm Visualizer",
        page_icon="📊",
        layout="wide"
    )

    st.title("🔄 Sorting Algorithm Visualizer")
    st.markdown("---")

    # Sidebar controls
    with st.sidebar:
        st.header("Controls")

        # Array size slider
        array_size = st.slider("Array Size", min_value=10, max_value=100, value=50, step=5)

        # Speed control
        speed = st.slider("Animation Speed (ms)", min_value=10, max_value=500, value=100, step=10)

        # Algorithm selection
        algorithm = st.selectbox(
            "Choose Sorting Algorithm",
            ["Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort", "Quick Sort"]
        )

        # Generate new array button
        if st.button("🎲 Generate New Array", type="primary"):
            st.session_state.array = np.random.randint(5, 200, array_size)
            st.session_state.sorted = False

        # Custom input
        st.subheader("Custom Array Input")
        custom_input = st.text_input("Enter numbers separated by commas:", placeholder="e.g., 64,34,25,12,22,11,90")

        if st.button("Add Custom Array"):
            try:
                custom_array = [int(x.strip()) for x in custom_input.split(',') if x.strip()]
                if custom_array:
                    st.session_state.array = np.array(custom_array)
                    st.session_state.sorted = False
                    st.success("Custom array loaded!")
                else:
                    st.error("Please enter valid numbers.")
            except ValueError:
                st.error("Please enter valid numbers separated by commas.")

    # Initialize array if not exists
    if 'array' not in st.session_state:
        st.session_state.array = np.random.randint(5, 200, array_size)
        st.session_state.sorted = False

    # Main content area
    col1, col2 = st.columns([3, 1])

    with col1:
        # Display current array
        st.subheader("Current Array")
        array_container = st.empty()

        # Visualization placeholder
        chart_container = st.empty()

        # Display array as bar chart
        fig, ax = plt.subplots(figsize=(12, 6))
        bars = ax.bar(range(len(st.session_state.array)), st.session_state.array, color='steelblue')
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
        ax.set_title(f'Array Visualization - {algorithm}')

        # Add value labels on bars
        for i, bar in enumerate(bars):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2., height + 1,
                    f'{int(height)}', ha='center', va='bottom', fontsize=8)

        chart_container.pyplot(fig)
        plt.close()

    with col2:
        st.subheader("Array Information")
        st.metric("Array Size", len(st.session_state.array))
        st.metric("Min Value", int(np.min(st.session_state.array)))
        st.metric("Max Value", int(np.max(st.session_state.array)))

        if st.session_state.sorted:
            st.success("✅ Array is sorted!")
        else:
            st.info("🔄 Array is unsorted")

    # Sort button
    st.markdown("---")
    if st.button(f"🚀 Start {algorithm}", type="primary", use_container_width=True):
        if not st.session_state.sorted:
            sort_and_visualize(algorithm, st.session_state.array.copy(), speed, chart_container)
            st.session_state.sorted = True
        else:
            st.warning("Array is already sorted! Generate a new array to sort again.")


def sort_and_visualize(algorithm, array, speed, container):
    """Visualize the sorting process step by step"""

    progress_bar = st.progress(0)
    status_text = st.empty()

    if algorithm == "Bubble Sort":
        steps = list(bubble_sort(array))
    elif algorithm == "Insertion Sort":
        steps = list(insertion_sort(array))
    elif algorithm == "Selection Sort":
        steps = list(selection_sort(array))
    elif algorithm == "Merge Sort":
        steps = list(merge_sort(array))
    elif algorithm == "Quick Sort":
        steps = list(quick_sort(array))

    total_steps = len(steps)

    for i, (current_array, comparing_indices, swapping_indices) in enumerate(steps):
        # Update progress
        progress = (i + 1) / total_steps
        progress_bar.progress(progress)
        status_text.text(f"Step {i + 1} of {total_steps}")

        # Create visualization
        fig, ax = plt.subplots(figsize=(12, 6))

        # Color bars based on their status
        colors = ['steelblue'] * len(current_array)

        # Highlight comparing elements
        if comparing_indices:
            for idx in comparing_indices:
                if idx < len(colors):
                    colors[idx] = 'red'

        # Highlight swapping elements
        if swapping_indices:
            for idx in swapping_indices:
                if idx < len(colors):
                    colors[idx] = 'orange'

        bars = ax.bar(range(len(current_array)), current_array, color=colors)
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
        ax.set_title(f'{algorithm} - Step {i + 1}')

        # Add value labels
        for j, bar in enumerate(bars):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2., height + 1,
                    f'{int(height)}', ha='center', va='bottom', fontsize=8)

        container.pyplot(fig)
        plt.close()

        # Control animation speed
        time.sleep(speed / 1000.0)

    progress_bar.progress(1.0)
    status_text.text("✅ Sorting completed!")
    st.balloons()


if __name__ == "__main__":
    main()
