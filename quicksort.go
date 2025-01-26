package main

import (
	"fmt"
	"math/rand"
	"time"

	"gonum.org/v1/plot"
	"gonum.org/v1/plot/plotter"
	"gonum.org/v1/plot/vg"
)

// QuickSort sorts an array using the quicksort algorithm and counts the steps.
func QuickSort(arr []int) ([]int, int) {
	countSteps := 0
	if len(arr) <= 1 {
		return arr, countSteps
	}
	pivot := arr[len(arr)-1]
	leftSide := []int{}
	rightSide := []int{}

	for _, x := range arr[:len(arr)-1] {
		if x <= pivot {
			leftSide = append(leftSide, x)
		} else {
			rightSide = append(rightSide, x)
		}
		countSteps++
	}

	leftSorted, leftSteps := QuickSort(leftSide)
	rightSorted, rightSteps := QuickSort(rightSide)
	countSteps += leftSteps + rightSteps + len(arr) - 1

	return append(append(leftSorted, pivot), rightSorted...), countSteps
}

func main() {
	// Input sizes to test
	inputSizes := []int{100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000}
	executionTimes := make([]float64, len(inputSizes))
	stepsCount := make([]int, len(inputSizes))

	// Measure execution times for different input sizes
	for i, size := range inputSizes {
		// Generate random input data
		inputArray := make([]int, size)
		for j := 0; j < size; j++ {
			inputArray[j] = rand.Intn(size)
		}
		// Measure execution time
		startTime := time.Now()
		_, steps := QuickSort(inputArray)
		elapsedTime := time.Since(startTime)

		executionTimes[i] = elapsedTime.Seconds() // Time in seconds
		stepsCount[i] = steps
	}

	// Create and save the plot
	if err := plotQuickSortExecutionTime(inputSizes, executionTimes); err != nil {
		fmt.Println("Error creating plot: ", err)
	} else {
		fmt.Println("Plot saved as 'QuickSort_ExecutionTimeGO.png'")
	}
}

// plotExecutionTime creates a plot of execution time vs input size and saves it.
func plotQuickSortExecutionTime(inputSizes []int, executionTimes []float64) error {
	// Create a new plot
	NewPlot := plot.New()

	// Set plot title and labels
	NewPlot.Title.Text = "QuickSort: Execution Time vs Input Size"
	NewPlot.X.Label.Text = "Input Size"
	NewPlot.Y.Label.Text = "Execution Time (Seconds)"

	// Create data points for the plot
	DataPoints := make(plotter.XYs, len(inputSizes))
	for i := range inputSizes {
		DataPoints[i].X = float64(inputSizes[i])
		DataPoints[i].Y = executionTimes[i]
	}

	// Create a line plot
	line, err := plotter.NewLine(DataPoints)
	if err != nil {
		return err
	}
	NewPlot.Add(line)

	// Save the plot as an image
	return NewPlot.Save(6*vg.Inch, 4*vg.Inch, "QuickSort_ExecutionTimeGO.png")
}
