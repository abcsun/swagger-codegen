#!/bin/sh

SCRIPT="$0"
SCALA_RUNNER_VERSION=$(scala ./bin/Version.scala)

while [ -h "$SCRIPT" ] ; do
  ls=`ls -ld "$SCRIPT"`
  link=`expr "$ls" : '.*-> \(.*\)$'`
  if expr "$link" : '/.*' > /dev/null; then
    SCRIPT="$link"
  else
    SCRIPT=`dirname "$SCRIPT"`/"$link"
  fi
done

if [ ! -d "${APP_DIR}" ]; then
  APP_DIR=`dirname "$SCRIPT"`/..
  APP_DIR=`cd "${APP_DIR}"; pwd`
fi

cd $APP_DIR


# if you've executed sbt assembly previously it will use that instead.
ags="com.wordnik.swagger.codegen.spec.Validator $@"

if [ -f $APP_DIR/target/scala-$SCALA_RUNNER_VERSION/*.jar ]; then
  scala -cp target/scala-$SCALA_RUNNER_VERSION/*.jar $ags
else
  echo "Please set scalaVersion := \"$SCALA_RUNNER_VERSION\" in build.sbt and run ./sbt assembly"
fi
