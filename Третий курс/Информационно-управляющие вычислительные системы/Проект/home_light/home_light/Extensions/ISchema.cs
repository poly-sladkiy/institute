using Microsoft.OpenApi.Any;
using Microsoft.OpenApi.Models;
using Swashbuckle.AspNetCore.SwaggerGen;
using System;

namespace home_light.Extensions
{
    /// <summary>
    /// Схема по умолчанию
    /// </summary>
    public class AddSchemaDefaultValues : ISchemaFilter
    {
        /// <summary>
        /// Применить схему форматирования
        /// </summary>
        /// <param name="schema"></param>
        /// <param name="context"></param>
        public void Apply(OpenApiSchema schema, SchemaFilterContext context)
        {
            Type listType = context.Type;
            if (typeof(ISchema).IsAssignableFrom(listType))
            {
                var instance = Activator.CreateInstance(listType);
                if(instance!=null)
                    schema.Example = ((ISchema)instance).GetDefaultValue();
            }
        }
    }
    /// <summary>
    /// Базовый интерфейс для реализации механизма значений по умолчанию для схемы
    /// </summary>
    interface ISchema
    {
        IOpenApiAny GetDefaultValue();
    }
}
