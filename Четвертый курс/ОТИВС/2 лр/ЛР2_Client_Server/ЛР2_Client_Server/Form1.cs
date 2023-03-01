using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
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
        int[] STOP_;//
        string[] S_;
        int[,] rools_;
        

        private void Form1_Load(object sender, EventArgs e)
        {
            // массив событий порождающего сценария множества S
            S_ = new string[100];// параметр: настроеное на 100 проодукционных праввил с 3 исходами
            S_[1] = "Data Science ?";
            S_[2] = "Gamedev ?";
            S_[3] = "Big company?";
            S_[4] = "Web?";
            S_[5] = "Fullstack?";
            S_[6] = "Back-end?";
            S_[7] = "ASP.Net Core";
            S_[8] = "Angular";
            S_[9] = "R";
            S_[10] = "Unreal Engine";
            S_[11] = "C# Unity";
            S_[12] = "Python Django";
            S_[13] = "Native?";
            S_[14] = "Android?";
            S_[15] = "Flutter";
            S_[16] = "Kotlin";
            S_[17] = "Swift";
            // закодированные логические правила: продукционная БЗ начало
            //int[,] rools_ = new int[100, 2];// параметр: настроеное на 100 проодукционных праввил с 3 исходами
            rools_ = new int[100, 2];// параметр: настроеное на 100 проодукционных праввил с 3 исходами
            //
            rools_[1, 1] = 9;// кодируем правило if S1 and R1 (да) then S9
            rools_[1, 0] = 2;// кодируем правило if S1 and R0 (нет) then S2
            rools_[2, 1] = 3;// кодируем правило if S1 and R1 then S3
            rools_[2, 0] = 4;// кодируем правило if S1 and R0 then S4 *
            rools_[3, 1] = 10;// кодируем правило if S1 and R1 then S6
            rools_[3, 0] = 11;// кодируем правило if S1 and R0 then S5 *        
            rools_[4, 1] = 5;// кодируем правило if S1 and R1 then S7-
            rools_[4, 0] = 13;// кодируем правило if S1 and R0 then S8 *
            rools_[5, 1] = 12;// кодируем правило if S1 and R1 then S10
            rools_[5, 0] = 6;// кодируем правило if S1 and R0 then S11*
            rools_[6, 1] = 7;// кодируем правило if S1 and R1 then S12*
            rools_[6, 0] = 8;// кодируем правило if S1 and R0 then S13*
			rools_[13, 1] = 14;// кодируем правило if S1 and R1 then S12*
            rools_[13, 0] = 15;// кодируем правило if S1 and R0 then S13*
            rools_[14, 1] = 16;// кодируем правило if S1 and R0 then S13*
            rools_[14, 0] = 17;// кодируем правило if S1 and R0 then S13*



            // закодированные логические правила: продукционная БЗ окончание
            //подготавливаем хранилище индексов концевых событий начало
            STOP_ = new int[100];// параметр: настроеное на 100 проодукционных праввил с 3 исходами

            // при отрацательном значении массива STOP_ событие концевое
            // метим концевые собятия
            for (int i = 0; i < 100; i++)
            {
                STOP_[i] = 7;
            }

            STOP_[9] = -7;
            STOP_[11] = -7;
            STOP_[10] = -7;
            STOP_[15] = -7;
            STOP_[17] = -7;
            STOP_[16] = -7;
            STOP_[8] = -7;
            STOP_[7] = -7;
            STOP_[12] = -7;
            
            // метим концевые собятия
            //подготавливаем хранилище индексов концевых событий окончание
            // инициализация стартового события
            
            textBox1.Text = S_[1];
            textBox3.Text = "1";
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

            //База фактов из 2-х переменных начало
            int SDB = 0;// антецедент импликации Si - левая часть правила
            int RDB = 0;// антецедент импликации Rj  - левая часть правила
            int S_cos_ = 0;// косеквент импликации
            //наполнение БФ информацией о состоянии предметной области начало
            SDB = Int32.Parse(textBox3.Text);
            RDB = Int32.Parse(textBox2.Text);
            //наполнение БФ информацией о состоянии предметной области окончание
            //База фактов из 2-х переменных окончание
                       

            

            

            // процедуры событий  !! события отделены от правил и процедур вывода!
            // интерпретатор начало // в явном виде нет цикла
            S_cos_ = rools_[SDB, RDB];
            // textBox2.Text = S_cos_.ToString();
            textBox4.Text = Convert.ToString(S_cos_);

            // интерпретатор окончение
            // button4_Click(sender, e);

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //string[] S_ = new string[100];// параметр: настроеное на 100 проодукционных праввил с 3 исходами
            
               

                        //********************************************************* код кнопки
          

            int S_cos_ = 0;// косеквент импликации
            //наполнение БФ информацией о состоянии предметной области начало
            S_cos_ = Int32.Parse(textBox4.Text);
            textBox1.Text = S_[S_cos_];
            textBox3.Text = Convert.ToString(S_cos_);


                if (STOP_[S_cos_] < 0)
                {
            MessageBox.Show("концевое событие");
            Environment.Exit(0);
             }
            
            
            
            //
            // дописать процедуру определения концевого события и окончания работы
           
            
        }

       
    }
}
