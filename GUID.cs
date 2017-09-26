using System;

namespace GUID
{
    class Program
    {
        static void Main(string[] args)
        {
            Guid guidValue = Guid.NewGuid();

            Console.WriteLine(guidValue.ToString());

            Console.WriteLine(guidValue.ToString('N')); // ハイフンなし

            Console.WriteLine(guidValue.ToString('B')); // { GUID }

            Console.WriteLine(guidValue.ToString('P')); // ( GUID )

            Console.WriteLine(guidValue.ToString(Guid.Empty)); // 0
        }
    }
}
