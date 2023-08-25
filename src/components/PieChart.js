import { Pie } from "react-chartjs-2";

import {
  Chart as ChartJS,
  Tooltip,
  Legend,
  ArcElement
} from "chart.js";
import ChartDataLabels from 'chartjs-plugin-datalabels';


import useMediaQuery from '@mui/material/useMediaQuery';


ChartJS.register(Tooltip, Legend, ArcElement, ChartDataLabels);

const PieChart = ({ data, chartName }) => {
  const chartData = {
    labels: Object.keys(data),
    datasets: [
      {
        label: chartName,
        data: Object.values(data),
        backgroundColor: [
          "rgba(255, 99, 132, 0.2)",
          "rgba(255, 159, 64, 0.2)",
          "rgba(255, 205, 86, 0.2)",
          "rgba(75, 192, 192, 0.2)",
          "rgba(54, 162, 235, 0.2)",
          "rgba(153, 102, 255, 0.2)",
          "rgba(201, 203, 207, 0.2)",
        ],
        borderColor: [
          "rgb(255, 99, 132)",
          "rgb(255, 159, 64)",
          "rgb(255, 205, 86)",
          "rgb(75, 192, 192)",
          "rgb(54, 162, 235)",
          "rgb(153, 102, 255)",
          "rgb(201, 203, 207)",
        ],
        borderWidth: 1,
      },
    ],
  };

  const isMobile = useMediaQuery('(max-width:600px)');

  const options = {
    responsive: true,
    plugins: {
      datalabels: {
        formatter: (value, context) => {
          let label = context.chart.data.labels[context.dataIndex];
          label = label.split('(')[0].trim(); // Split the label at the first '(' and take the first part
          return label + ': ' + value;
        },
        color: '#000',
        // anchor: 'end',
        align: 'end',
        offset: isMobile ? 0 : 100,
      },
    },
  };

  
  

  return (
    <div style={{ width: isMobile ? "100vw": "30vw" }}>
      <h3>{chartName}</h3>
      <Pie data={chartData} options={options} />
      <pre>{JSON.stringify(data, null, 4)}</pre>
    </div>
  );
};

export default PieChart;