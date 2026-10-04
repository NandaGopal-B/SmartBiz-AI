async function loadDashboard(){
  try{
    const summary = await fetch('/api/analytics/summary').then(r=>r.json());
    document.getElementById('customers').textContent = summary.customers.toLocaleString();
    document.getElementById('products').textContent = summary.products.toLocaleString();
    document.getElementById('orders').textContent = summary.orders.toLocaleString();
    document.getElementById('revenue').textContent = '₹' + Number(summary.revenue).toLocaleString();
    const health = await fetch('/api/health').then(r=>r.json());
    document.getElementById('status').textContent = '● API Online — ' + health.service;
  }catch(e){
    document.getElementById('status').textContent = '● API unavailable — start FastAPI with uvicorn backend.main:app --reload';
    document.getElementById('status').style.background = '#fff2f0';
    document.getElementById('status').style.color = '#b42318';
  }
}
loadDashboard();
