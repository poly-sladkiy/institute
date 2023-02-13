using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication2
{
	class Program
	{
		static void Main(string[] args)
		{
			string? result;
		
			///////////// s1
			Console.WriteLine("S1 Data Science [y/n]?");
			result = Console.ReadLine();

			if (result.Equals("y"))
			{//if (result.Equals("1"))
				goto S9;
			}
			else// ветка по нет
			{
				goto S2;
			}

			S2:
			Console.WriteLine("S2 Gamedev [y/n]?");
			result = Console.ReadLine();

			if (result.Equals("y"))
			{//if (result.Equals("1"))
				goto S3;
			}
			else// ветка по нет
			{
				goto S4;
			}

			S3:
			Console.WriteLine("S3 Big company [y/n]?");
			result = Console.ReadLine();

			if (result.Equals("y"))
				goto S10;
			else
				goto S11;

			S4:
			Console.WriteLine("S4 Web development [y/n]?");
			result = Console.ReadLine();

			if (result.Equals("y"))
				goto S5;
			else
				goto S13;

			S5:
			Console.WriteLine("S5 Full stack [y/n]?");
			result = Console.ReadLine();

			if (result.Equals("y"))
				goto S12;
			else
				goto S6;

			S6:
			Console.WriteLine("S6 Backend [y/n]?");
			result = Console.ReadLine();

			if (result.Equals("y"))
				goto S7;
			else
				goto S8;

			S13:
			Console.WriteLine("S13 Native [y/n]?");
			result = Console.ReadLine();

			if (result.Equals("y"))
				goto S14;
			else
				goto S15;

			S14:
			Console.WriteLine("S14 Android [y/n]?");
			result = Console.ReadLine();

			if (result.Equals("y"))
				goto S16;
			else
				goto S17;

			S7:
			Console.WriteLine("R5 Language: C# Asp.NET Core");
			goto END_;

			S8:
			Console.WriteLine("R6 Language: Angular");
			goto END_;

			S9:
			Console.WriteLine("R1 Language: R");
			goto END_;

			S10:
			Console.WriteLine("R2 Language: C++ Unreal");
			goto END_;

			S11:
			Console.WriteLine("R3 Language: C# Unity");
			goto END_;

			S12:
			Console.WriteLine("R4 Language: Python Django");
			goto END_;

			S15:
			Console.WriteLine("R7 Language: Flutter");
			goto END_;

			S16:
			Console.WriteLine("R8 Language: Kotlin");
			goto END_;

			S17:
			Console.WriteLine("R9 Language: Swift");
			goto END_;

			END_: result = Console.ReadLine();
		}

	}
}

