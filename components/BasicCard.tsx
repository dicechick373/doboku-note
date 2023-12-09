import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import CardHeader from '@mui/material/CardHeader';
import Grid from '@mui/material/Grid';
import Divider from '@mui/material/Divider';

const bull = (
  <Box
    component="span"
    sx={{ display: 'inline-block', mx: '2px', transform: 'scale(0.8)' }}
  >
    •
  </Box>
);

export default function BasicCard() {
  return (
    <Card sx={{ minWidth: 275 }}>
      <CardContent>
      <Box>
        <Typography sx={{ fontSize: 14 }} color="error.main" gutterBottom>
          最重要判例
        </Typography>
        <Typography variant="h6" component="div">
          タイトル
        </Typography>
        </Box>
        <Divider variant="middle" />
        <Grid container spacing={1}>
 

     
  <Grid item xs={2}>
    事案
  </Grid>
  <Grid item xs={10}>
    xs=49999999999999999999999999999999999999999999999999999999999999999
  </Grid>
  <Grid item xs={2}>
    結論
  </Grid>
  <Grid item xs={10}>
    xs=89999999999999999999999999999999999999999999999999999999999999999999999999999999
  </Grid>
</Grid>

        <Typography variant="body2">
          well meaning and kindly.
          <br />
          {'"a benevolent smile"'}
        </Typography>
        
      </CardContent>
      <CardActions>
        <Button size="small">Learn More</Button>
      </CardActions>
    </Card>
  );
}