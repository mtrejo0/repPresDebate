import { Box, Grid } from "@mui/material";
import { useEffect, useState } from "react";
import PieChart from "./PieChart";

import wordCount from '../python/word_count.json';

import wordFreq from '../python/word_frequency.json';

export default function Home() {
  const [data, setData] = useState(wordCount);

  return (
    <Box>

      <Box sx={{ width: "100%" }}>
        {data && <PieChart data={data} chartName="Word Count" />}
      </Box>


      <Box mt={16}></Box>


      <h3>Word frequencies per candidate:</h3>

      <Grid container >
      {Object.entries(wordFreq).map((each: any) => <Grid item xs={6} md={4}>

        {each[0]}

        <pre>{JSON.stringify(each[1], null, 4)}</pre>
        
        </Grid>)}

        </Grid>
    </Box>
    
  );
}