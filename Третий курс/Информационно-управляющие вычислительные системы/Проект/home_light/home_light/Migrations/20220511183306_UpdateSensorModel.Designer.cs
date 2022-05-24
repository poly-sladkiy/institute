﻿// <auto-generated />
using System;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Migrations;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
using Npgsql.EntityFrameworkCore.PostgreSQL.Metadata;
using home_light;

#nullable disable

namespace home_light.Migrations
{
    [DbContext(typeof(ApplicationContext))]
    [Migration("20220511183306_UpdateSensorModel")]
    partial class UpdateSensorModel
    {
        protected override void BuildTargetModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder
                .HasAnnotation("ProductVersion", "6.0.4")
                .HasAnnotation("Relational:MaxIdentifierLength", 63);

            NpgsqlModelBuilderExtensions.UseIdentityByDefaultColumns(modelBuilder);

            modelBuilder.Entity("home_light.Models.Data", b =>
                {
                    b.Property<int>("Id")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("integer");

                    NpgsqlPropertyBuilderExtensions.UseIdentityByDefaultColumn(b.Property<int>("Id"));

                    b.Property<DateTime>("DateAdd")
                        .HasColumnType("timestamp with time zone");

                    b.Property<DateTime>("DateUpdate")
                        .HasColumnType("timestamp with time zone");

                    b.Property<bool>("IsDeleted")
                        .HasColumnType("boolean");

                    b.Property<bool>("IsWork")
                        .HasColumnType("boolean");

                    b.Property<int?>("SensorId")
                        .HasColumnType("integer");

                    b.HasKey("Id");

                    b.HasIndex("SensorId");

                    b.ToTable("Datas");
                });

            modelBuilder.Entity("home_light.Models.Flashlight", b =>
                {
                    b.Property<int>("Id")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("integer");

                    NpgsqlPropertyBuilderExtensions.UseIdentityByDefaultColumn(b.Property<int>("Id"));

                    b.Property<DateTime>("DateAdd")
                        .HasColumnType("timestamp with time zone");

                    b.Property<DateTime>("DateUpdate")
                        .HasColumnType("timestamp with time zone");

                    b.Property<bool>("IsDeleted")
                        .HasColumnType("boolean");

                    b.Property<string>("Name")
                        .HasColumnType("text");

                    b.Property<int?>("SensorId")
                        .HasColumnType("integer");

                    b.HasKey("Id");

                    b.HasIndex("SensorId");

                    b.ToTable("Flashlights");
                });

            modelBuilder.Entity("home_light.Models.Room", b =>
                {
                    b.Property<int>("Id")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("integer");

                    NpgsqlPropertyBuilderExtensions.UseIdentityByDefaultColumn(b.Property<int>("Id"));

                    b.Property<DateTime>("DateAdd")
                        .HasColumnType("timestamp with time zone");

                    b.Property<DateTime>("DateUpdate")
                        .HasColumnType("timestamp with time zone");

                    b.Property<bool>("IsDeleted")
                        .HasColumnType("boolean");

                    b.Property<string>("Name")
                        .HasColumnType("text");

                    b.HasKey("Id");

                    b.ToTable("Rooms");
                });

            modelBuilder.Entity("home_light.Models.Sensor", b =>
                {
                    b.Property<int>("Id")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("integer");

                    NpgsqlPropertyBuilderExtensions.UseIdentityByDefaultColumn(b.Property<int>("Id"));

                    b.Property<DateTime>("DateAdd")
                        .HasColumnType("timestamp with time zone");

                    b.Property<DateTime>("DateUpdate")
                        .HasColumnType("timestamp with time zone");

                    b.Property<bool>("IsDeleted")
                        .HasColumnType("boolean");

                    b.Property<bool>("IsShining")
                        .HasColumnType("boolean");

                    b.Property<string>("Name")
                        .HasColumnType("text");

                    b.Property<int?>("RoomId")
                        .HasColumnType("integer");

                    b.HasKey("Id");

                    b.HasIndex("RoomId");

                    b.ToTable("Sensors");
                });

            modelBuilder.Entity("home_light.Models.Data", b =>
                {
                    b.HasOne("home_light.Models.Sensor", "Sensor")
                        .WithMany("Data")
                        .HasForeignKey("SensorId");

                    b.Navigation("Sensor");
                });

            modelBuilder.Entity("home_light.Models.Flashlight", b =>
                {
                    b.HasOne("home_light.Models.Sensor", "Sensor")
                        .WithMany("Flashlights")
                        .HasForeignKey("SensorId");

                    b.Navigation("Sensor");
                });

            modelBuilder.Entity("home_light.Models.Sensor", b =>
                {
                    b.HasOne("home_light.Models.Room", "Room")
                        .WithMany("Sensors")
                        .HasForeignKey("RoomId");

                    b.Navigation("Room");
                });

            modelBuilder.Entity("home_light.Models.Room", b =>
                {
                    b.Navigation("Sensors");
                });

            modelBuilder.Entity("home_light.Models.Sensor", b =>
                {
                    b.Navigation("Data");

                    b.Navigation("Flashlights");
                });
#pragma warning restore 612, 618
        }
    }
}
