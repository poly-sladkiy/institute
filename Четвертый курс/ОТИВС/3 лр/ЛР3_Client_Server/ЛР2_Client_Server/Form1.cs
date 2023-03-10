using System;
using System.Data;
using System.Windows.Forms;
using System.Data.SqlClient;


namespace ЛР2_Client_Server
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //SELECT        ID, Sl, Ind_Stop FROM            dbo.Events WHERE        (Ind_Stast = 1)
            DataSet ds = new DataSet();// создаем объект DataSet ds = new DataSet();// создаем объект 
            string connectionString = @"Data Source=localhost;Initial Catalog=OTIVS;User Id=sa;Password=QZWXECRVasdf1234!;";// создаем строку подключения

            string commandString = "SELECT        ID, SI, Ind_Stop FROM            dbo.Events WHERE        (Ind_Start = 1)";// создаем запрос

            SqlDataAdapter adapter = new SqlDataAdapter(commandString, connectionString);// создаем SqlDataAdapter adapter

            adapter.Fill(ds); // заполнение DataSet данными с помощью DataAdapter


            // узнаем число строк в объекте ds.Tables[0] 
            int rows_ = 0;
            rows_ = ds.Tables[0].Rows.Count;
            if (rows_ > 0)
            {//if (rows_ > 0)
                  DataRow row = ds.Tables[0].Rows[0]; ; //в объект DataRow записали j-й ряд таблицы DataTable
                  string ii_str; // задали стринговую переменную
                  ii_str = row["SI"].ToString();// значение поля до изменения
                  textBox1.Text = ii_str;
                  ii_str = row["ID"].ToString();// значение поля до изменения
                  textBox3.Text = ii_str;
            } //if (rows_ > 0)
     }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            textBox2.Text = "1";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox2.Text = "0";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //
            DataSet ds = new DataSet();// создаем объект DataSet ds = new DataSet();// создаем объект 
            string Rj__; // задали стринговую переменную
            //Si
            string Si__; // задали стринговую переменную
            Rj__ = textBox2.Text;
            Si__ = textBox3.Text;
            string connectionString = @"Data Source=localhost;Initial Catalog=OTIVS;User Id=sa;Password=QZWXECRVasdf1234!;";// создаем строку подключения
            string commandString = "SELECT        TOP (100) PERCENT ID, Si, Rj, Sk, Memo  FROM            dbo.Rools WHERE        (Si =" + Si__ + ") AND (Rj =" + Rj__ + ")";// создаем запрос
            SqlDataAdapter adapter = new SqlDataAdapter(commandString, connectionString);// создаем SqlDataAdapter adapter
            adapter.Fill(ds); // заполнение DataSet данными с помощью DataAdapter
            // узнаем число строк в объекте ds.Tables[0] 
            int rows_ = 0;
            rows_ = ds.Tables[0].Rows.Count;
            if (rows_ > 0)
            {//if (rows_ > 0)
                DataRow row = ds.Tables[0].Rows[0]; ; //в объект DataRow записали j-й ряд таблицы DataTable
                string ii_str; // задали стринговую переменную
                ii_str = row["Sk"].ToString();// значение поля до изменения
                textBox4.Text = ii_str;
                
            } //if (rows_ > 0)
            button4_Click(sender, e);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //SELECT        ID, Sl, Ind_Stop FROM            dbo.Events WHERE        (Ind_Stast = 1)
            DataSet ds = new DataSet();// создаем объект DataSet ds = new DataSet();// создаем объект 
            string connectionString = @"Data Source=localhost;Initial Catalog=OTIVS;User Id=sa;Password=QZWXECRVasdf1234!;";// создаем строку подключения


            string S__NEXT; // задали стринговую переменную
            string STOP_; // задали стринговую переменную
            
            S__NEXT = textBox4.Text;

            string commandString = "SELECT        ID, SI, Ind_Stop  FROM            dbo.Events  WHERE        (ID = " + S__NEXT  + ")";// создаем запрос

            SqlDataAdapter adapter = new SqlDataAdapter(commandString, connectionString);// создаем SqlDataAdapter adapter

            adapter.Fill(ds); // заполнение DataSet данными с помощью DataAdapter

            //tb4
            
            // узнаем число строк в объекте ds.Tables[0] 
            int rows_ = 0;
            rows_ = ds.Tables[0].Rows.Count;
            if (rows_ > 0)
            {//if (rows_ > 0)
                DataRow row = ds.Tables[0].Rows[0]; ; //в объект DataRow записали j-й ряд таблицы DataTable
                string ii_str; // задали стринговую переменную
                ii_str = row["SI"].ToString();// значение поля до изменения
                textBox1.Text = ii_str;
                ii_str = row["ID"].ToString();// значение поля до изменения
                textBox3.Text = ii_str;
                ii_str = row["Ind_Stop"].ToString();
                STOP_=ii_str;
                if (STOP_ == "True")
                {
                    MessageBox.Show("концевое событие");
                }

            } //if (rows_ > 0)
        }  
    }
}
