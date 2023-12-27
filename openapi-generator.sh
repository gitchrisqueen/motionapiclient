#!/usr/bin/env bash

# Load env variables (in the .env file)
#set -o allexport
#source .env
#set +o allexport

#DEFAULT VALUES
PACKAGE_NAME="usemotion_api_client"
PACKAGE_URL="https://github.com/gitchrisqueen/usemotion-api-client"
PACKAGE_VERSION="1.0.4"
PROJECT_NAME="usemotion_api_client"
ISO_DATE_FORMAT="%Y-%m-%d"
ISO_DATETIME_FORMAT="%Y-%m-%dT%H:%M:%S%z"
USEONEOFDISCRIMINATORLOOKUP="true"
GIT_USER="gitchrisqueen"
GIT_REPO="usemotion-api-client"
CONFIG_OPTIONS="appName=Motion REST API Client,infoName=Christopher Queen,infoEmail=christopher.queen@gmail.com,dateFormat=$ISO_DATE_FORMAT,datetimeFormat=$ISO_DATETIME_FORMAT,packageName=$PACKAGE_NAME,packageUrl=$PACKAGE_URL,packageVersion=$PACKAGE_VERSION,projectName=$PROJECT_NAME,useOneOfDiscriminatorLookup=$USEONEOFDISCRIMINATORLOOKUP"
RELEASE_NOTE="OpenAPI client code auto-generated for version $PACKAGE_VERSION"
P1_PATH="use-motion-api-pydantic-1"
P2_PATH="use-motion-api-pydantic-2"
P1_TAG="p1_$PACKAGE_VERSION"
P2_TAG="p2_$PACKAGE_VERSION"
INPUT_FILE="https://stoplight.io/api/v1/projects/motion/motion-rest-api/nodes/swagger.json"
CURRENT_PATH=$(pwd)
GENERATOR="python" # Use python | python-pydantic-v1

export PYTHON_POST_PROCESS_FILE="$(which yapf) -i"

# Create pydantic v2 version of code
echo "Generating v$PACKAGE_VERSION pydantic v2 code"
openapi-generator generate --git-host github.com --git-repo-id $GIT_REPO --git-user-id $GIT_USER --enable-post-process-file \
 -g $GENERATOR -i $INPUT_FILE -o ./ --additional-properties="$CONFIG_OPTIONS"

exit 1

# Tag and Push
(
echo "Git creating tag $P2_TAG" && \
git tag "$P2_TAG" && \
echo "Git pushing tag $P2_TAG" && \
git push origin "$P2_TAG"
)
