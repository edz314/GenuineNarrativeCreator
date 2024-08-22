import datetime
import statistics

class ReportGenerator:
    """
    Generates detailed reports on the performance of advertised products within the game. 
    The reports include metrics on brand immersion, player engagement, and the overall 
    effectiveness of the advertising strategy.
    """

    def __init__(self):
        """
        Initializes the ReportGenerator object, setting up necessary configurations.
        """
        self.default_metrics = [
            "total_interactions", 
            "average_brand_immersion", 
            "engagement_duration", 
            "audience_reach", 
            "conversion_rate"
        ]

    def generate_report(self, data, custom_metrics=None):
        """
        Generates a report based on the provided data.

        Args:
            data (list of dicts): A list of data points collected from player interactions.
            custom_metrics (list of str, optional): A list of custom metrics to include in the report.

        Returns:
            str: A string containing the generated report.
        """
        metrics = custom_metrics if custom_metrics else self.default_metrics
        report = f"Advertising Performance Report\nGenerated on: {datetime.datetime.now()}\n\n"

        # Generate each section of the report based on the chosen metrics
        for metric in metrics:
            if metric == "total_interactions":
                report += self._total_interactions(data) + "\n"
            elif metric == "average_brand_immersion":
                report += self._average_brand_immersion(data) + "\n"
            elif metric == "engagement_duration":
                report += self._engagement_duration(data) + "\n"
            elif metric == "audience_reach":
                report += self._audience_reach(data) + "\n"
            elif metric == "conversion_rate":
                report += self._conversion_rate(data) + "\n"
            else:
                report += f"{metric}: Custom metric not recognized or not implemented.\n"

        # Add a summary or conclusions section if needed
        report += self._generate_summary(data)
        return report

    def _total_interactions(self, data):
        """
        Calculates the total number of interactions with the advertised products.

        Args:
            data (list of dicts): The collected data points.

        Returns:
            str: A string summarizing the total interactions.
        """
        total = len(data)
        return f"Total Interactions: {total}"

    def _average_brand_immersion(self, data):
        """
        Calculates the average brand immersion score.

        Args:
            data (list of dicts): The collected data points.

        Returns:
            str: A string summarizing the average brand immersion.
        """
        immersion_scores = [d.get('brand_immersion', 0) for d in data]
        average_immersion = statistics.mean(immersion_scores) if immersion_scores else 0
        return f"Average Brand Immersion: {average_immersion:.2f}"

    def _engagement_duration(self, data):
        """
        Calculates the average duration of player engagement with the advertised products.

        Args:
            data (list of dicts): The collected data points.

        Returns:
            str: A string summarizing the average engagement duration.
        """
        durations = [d.get('engagement_duration', 0) for d in data]
        average_duration = statistics.mean(durations) if durations else 0
        return f"Average Engagement Duration: {average_duration:.2f} minutes"

    def _audience_reach(self, data):
        """
        Estimates the audience reach based on the number of unique players who interacted with the advertisement.

        Args:
            data (list of dicts): The collected data points.

        Returns:
            str: A string summarizing the audience reach.
        """
        unique_users = {d.get('user_id') for d in data if d.get('user_id')}
        reach = len(unique_users)
        return f"Audience Reach: {reach} unique players"

    def _conversion_rate(self, data):
        """
        Calculates the conversion rate based on the number of players who took a specific desired action (e.g., purchase).

        Args:
            data (list of dicts): The collected data points.

        Returns:
            str: A string summarizing the conversion rate.
        """
        conversions = sum(1 for d in data if d.get('conversion') is True)
        total_interactions = len(data)
        conversion_rate = (conversions / total_interactions) * 100 if total_interactions else 0
        return f"Conversion Rate: {conversion_rate:.2f}%"

    def _generate_summary(self, data):
        """
        Generates a summary section for the report.

        Args:
            data (list of dicts): The collected data points.

        Returns:
            str: A string containing the summary of findings and recommendations.
        """
        # Example summary content
        return "\nSummary:\nThe advertising campaign has shown strong engagement with an impressive audience reach. " \
               "The average brand immersion is high, indicating that players found the integration meaningful. " \
               "However, the conversion rate could be improved by refining the call-to-action within the game environment."

    def add_custom_metric(self, metric_name, metric_function):
        """
        Adds a custom metric to the report generator.

        Args:
            metric_name (str): The name of the metric to add.
            metric_function (function): A function that calculates and returns a string for the metric.

        Raises:
            ValueError: If the metric function is not callable.
        """
        if callable(metric_function):
            setattr(self, f"_{metric_name}", metric_function)
        else:
            raise ValueError("Metric function must be callable.")

    def remove_custom_metric(self, metric_name):
        """
        Removes a custom metric from the report generator.

        Args:
            metric_name (str): The name of the metric to remove.

        Raises:
            AttributeError: If the metric does not exist.
        """
        if hasattr(self, f"_{metric_name}"):
            delattr(self, f"_{metric_name}")
        else:
            raise AttributeError(f"No such metric: {metric_name}")

    def update_default_metrics(self, new_metrics):
        """
        Updates the list of default metrics used in report generation.

        Args:
            new_metrics (list of str): A list of new default metrics.
        """
        if isinstance(new_metrics, list) and all(isinstance(metric, str) for metric in new_metrics):
            self.default_metrics = new_metrics
        else:
            raise ValueError("new_metrics must be a list of strings.")

    def reset_to_default_metrics(self):
        """
        Resets the metrics to the default set.
        """
        self.default_metrics = [
            "total_interactions", 
            "average_brand_immersion", 
            "engagement_duration", 
            "audience_reach", 
            "conversion_rate"
        ]
