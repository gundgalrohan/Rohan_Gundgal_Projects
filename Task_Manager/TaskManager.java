import java.util.ArrayList;
import java.util.Comparator;
import java.util.Scanner;

class Task {
    private final String title;
    private boolean isCompleted;
    private String priority;  // Low, Medium, High

    public Task(String title, String priority) {
        this.title = title;
        this.isCompleted = false;
        this.priority = priority;
    }

    public String getTitle() {
        return title;
    }

    public boolean isCompleted() {
        return isCompleted;
    }

    public void markCompleted() {
        isCompleted = true;
    }

    public String getPriority() {
        return priority;
    }

    @Override
    public String toString() {
        return title + " - " + (isCompleted ? "Completed" : "Not Completed") + " - Priority: " + priority;
    }
}

public class TaskManager {
    private static final ArrayList<Task> tasks = new ArrayList<>();
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int choice;
        do {
            printMenu();
            choice = getChoice();
            switch (choice) {
                case 1:
                    addTask();
                    break;
                case 2:
                    viewTasks();
                    break;
                case 3:
                    markTaskComplete();
                    break;
                case 4:
                    deleteTask();
                    break;
                case 5:
                    editTask();
                    break;
                case 6:
                    filterTasks();
                    break;
                case 7:
                    sortTasksByPriority();
                    break;
                case 8:
                    System.out.println("Exiting Task Manager...");
                    break;
                default:
                    System.out.println("Invalid option. Try again.");
            }
        } while (choice != 8);
    }

    private static void printMenu() {
        System.out.println("\n=== TASK MANAGER ===");
        System.out.println("1. Add Task");
        System.out.println("2. View All Tasks");
        System.out.println("3. Mark Task as Completed");
        System.out.println("4. Delete Task");
        System.out.println("5. Edit Task");
        System.out.println("6. Filter Tasks by Status");
        System.out.println("7. Sort Tasks by Priority");
        System.out.println("8. Exit");
        System.out.print("Choose an option: ");
    }

    private static int getChoice() {
        try {
            return Integer.parseInt(scanner.nextLine());
        } catch (NumberFormatException e) {
            return -1; // invalid input
        }
    }

    private static void addTask() {
        System.out.print("Enter task title: ");
        String title = scanner.nextLine();
        System.out.print("Enter task priority (Low, Medium, High): ");
        String priority = scanner.nextLine();
        // Validate priority input
        while (!(priority.equalsIgnoreCase("Low") || priority.equalsIgnoreCase("Medium") || priority.equalsIgnoreCase("High"))) {
            System.out.println("Invalid priority! Please enter Low, Medium, or High.");
            System.out.print("Enter task priority (Low, Medium, High): ");
            priority = scanner.nextLine();
        }
        tasks.add(new Task(title, priority));
        System.out.println("Task added!");
    }

    private static void viewTasks() {
        if (tasks.isEmpty()) {
            System.out.println("No tasks available.");
            return;
        }
        System.out.println("\nYour Tasks:");
        for (int i = 0; i < tasks.size(); i++) {
            System.out.println((i + 1) + ". " + tasks.get(i));
        }
    }

    private static void markTaskComplete() {
        viewTasks();
        if (tasks.isEmpty()) return;
        System.out.print("Enter task number to mark complete: ");
        int num = getChoice();
        if (num > 0 && num <= tasks.size()) {
            tasks.get(num - 1).markCompleted();
            System.out.println("Task marked as completed.");
        } else {
            System.out.println("Invalid task number.");
        }
    }

    private static void deleteTask() {
        viewTasks();
        if (tasks.isEmpty()) return;
        System.out.print("Enter task number to delete: ");
        int num = getChoice();
        if (num > 0 && num <= tasks.size()) {
            tasks.remove(num - 1);
            System.out.println("Task deleted.");
        } else {
            System.out.println("Invalid task number.");
        }
    }

    private static void editTask() {
        viewTasks();
        if (tasks.isEmpty()) return;
        System.out.print("Enter task number to edit: ");
        int num = getChoice();
        if (num > 0 && num <= tasks.size()) {
            Task task = tasks.get(num - 1);
            System.out.print("Enter new title for task: ");
            String newTitle = scanner.nextLine();
            task = new Task(newTitle, task.getPriority());  // Creating new task with updated title
            tasks.set(num - 1, task);  // Updating task in list
            System.out.println("Task updated.");
        } else {
            System.out.println("Invalid task number.");
        }
    }

    private static void filterTasks() {
        System.out.println("Filter tasks by status:");
        System.out.println("1. Completed");
        System.out.println("2. Not Completed");
        System.out.print("Choose an option: ");
        int choice = getChoice();
        if (choice == 1) {
            tasks.stream().filter(Task::isCompleted).forEach(System.out::println);
        } else if (choice == 2) {
            tasks.stream().filter(task -> !task.isCompleted()).forEach(System.out::println);
        } else {
            System.out.println("Invalid option.");
        }
    }

    private static void sortTasksByPriority() {
        tasks.sort(Comparator.comparing(Task::getPriority));
        System.out.println("Tasks sorted by priority.");
    }
}
