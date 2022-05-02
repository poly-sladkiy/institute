using System.Linq.Expressions;
using System.Reflection;

namespace home_light.Extensions
{
    /// <summary>
    /// Расширения для коллекций
    /// </summary>
    public static class EnumerableExtensions
    {
        /// <summary>
        /// Пермещать список
        /// </summary>
        /// <typeparam name="T"></typeparam>
        /// <param name="source"></param>
        /// <returns></returns>
        public static IEnumerable<T> Randomize<T>(this IEnumerable<T> source)
        {
            Random rnd = new();
            return source.OrderBy((item) => rnd.Next());
        }
        /// <summary>
        /// Получение свойства по названию
        /// </summary>
        /// <param name="objType"></param>
        /// <param name="name"></param>
        /// <returns></returns>
        private static PropertyInfo GetPropertyInfo(Type objType, string name)
        {
            var properties = objType.GetProperties();
            var matchedProperty = properties.FirstOrDefault(p => p.Name.ToLower() == name.ToLower());
            if (matchedProperty == null)
                throw new ArgumentException("Недопустимое поле для сортировки");

            return matchedProperty;
        }
        /// <summary>
        /// 
        /// </summary>
        /// <param name="objType"></param>
        /// <param name="pi"></param>
        /// <returns></returns>
        private static LambdaExpression GetOrderExpression(Type objType, PropertyInfo pi)
        {
            var paramExpr = Expression.Parameter(objType);
            var propAccess = Expression.PropertyOrField(paramExpr, pi.Name);
            var expr = Expression.Lambda(propAccess, paramExpr);
            return expr;
        }
        /// <summary>
        /// Сортировка расширение
        /// </summary>
        /// <typeparam name="T"></typeparam>
        /// <param name="query"></param>
        /// <param name="name"></param>
        /// <returns></returns>
        public static IQueryable<T>? OrderBy<T>(this IQueryable<T> query, string name)
        {
            var propInfo = GetPropertyInfo(typeof(T), name);
            var expr = GetOrderExpression(typeof(T), propInfo);

            var method = typeof(Queryable).GetMethods().FirstOrDefault(m => m.Name == "OrderBy" && m.GetParameters().Length == 2);
            var genericMethod = method?.MakeGenericMethod(typeof(T), propInfo.PropertyType);
            return (IQueryable<T>?)genericMethod?.Invoke(null, new object[] { query, expr });
        }
        /// <summary>
        /// Обратная сортировка расширение
        /// </summary>
        /// <typeparam name="T"></typeparam>
        /// <param name="query"></param>
        /// <param name="name"></param>
        /// <returns></returns>
        public static IQueryable<T>? OrderByDescending<T>(this IQueryable<T> query, string name)
        {
            var propInfo = GetPropertyInfo(typeof(T), name);
            var expr = GetOrderExpression(typeof(T), propInfo);

            var method = typeof(Queryable).GetMethods().FirstOrDefault(m => m.Name == "OrderByDescending" && m.GetParameters().Length == 2);
            var genericMethod = method?.MakeGenericMethod(typeof(T), propInfo.PropertyType);
            return (IQueryable<T>?)genericMethod?.Invoke(null, new object[] { query, expr });
        }
    }
}
